import sys
import click
import pyperclip
import json
import requests
import pretty_errors
import urllib
import warnings

from os import path
from bs4 import BeautifulSoup
from selenium import webdriver
from requests import RequestsDependencyWarning

settings = dict(
    allow_extra_args=True
)

@click.command(context_settings=settings)
@click.option('-c', '--copy-to-clipboard', is_flag=True, default=False)
@click.option('-l', '--links', is_flag=True, default=False)
@click.pass_context
def translate(context, copy_to_clipboard, links, filename=None, text=None):
    language_file_path = path.dirname(path.realpath(__file__)) + '/data/languages.json'
    language_file = open(language_file_path)
    languages = json.load(language_file)

    source, targets, subject = parse_arguments(context.args)

    if path.exists(subject):
        file = open(subject, 'r')
        text = file.read()
        file.close()
    else:
        text = subject

    if source is None:
        source = 'auto'

    google_translate_link = 'https://translate.google.com/?view=home&op=translate&sl={}&tl={}&text={}'

    translations = []
    for target in targets:
        target_code = languages[target.lower().capitalize()]

        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=RequestsDependencyWarning)
            translation_link = google_translate_link.format(source, target_code, urllib.parse.quote_plus(text))

        if links:
            translation = translation_link
        else:
            translation = get_translation(translation_link)
        
        translations.append((target.capitalize(), translation))

    output = ''
    for (target, translation) in translations:
        output += target + ':\n' + translation + '\n\n'
        print(target + ':')
        print(translation)
        print()

    if copy_to_clipboard:
        pyperclip.copy(output)
        print('Copied to clipboard')

def parse_arguments(arguments):
    source = None
    targets = []
    subject = ''

    expect = None

    while len(arguments) > 0:
        token = arguments.pop(0)
        
        if token == 'from' and expect != 'subject':
            expect = 'source'
            continue
        
        if token == 'to' and expect != 'subject':
            expect = 'target'
            continue

        if expect == 'source':
            source = token.strip(':')
            continue

        if expect == 'target':
            targets.append(token.strip(':').strip(','))

        if ':' in token:
            expect = 'subject'
            continue

        if expect == 'subject':
            subject += ' ' + token
            subject = subject.strip()
            continue

    return (source, targets, subject)

def get_translation(link):
    """user_agent = "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"

    response = requests.get(link, headers={
        'User-Agent': user_agent
    })

    content = response.content"""

    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
    driver.get(link)

    content = driver.page_source

    soup = BeautifulSoup(content, features='lxml')
    container = soup.find(attrs={'class': 'tlid-translation translation'})

    return container.text
    

if __name__ == '__main__':
    translate()

sys.modules[__name__] = translate()