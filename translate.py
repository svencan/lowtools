import sys
import click
import pyperclip
import json

from os import path
from urllib import parse

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

    if not links:
        print('Can only give you links for now...')
        print()
        links = True

    if source is None:
        source = 'auto'

    google_translate_link = 'https://translate.google.com/?view=home&op=translate&sl={}&tl={}&text={}'

    translations = []
    for target in targets:

        target_code = languages[target.lower().capitalize()]

        if links:
            translation = google_translate_link.format(source, target_code, parse.quote(text))
        
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
        
        if token == 'from':
            expect = 'source'
            continue
        
        if token == 'to':
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
    

if __name__ == '__main__':
    translate()

sys.modules[__name__] = translate()