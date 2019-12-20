import sys
import click
import random
import pyperclip

settings = dict(
    allow_extra_args=True
)

@click.command(context_settings=settings)
@click.option('-c', '--copy-to-clipboard', is_flag=True, default=False)
@click.pass_context
def rcase(context, copy_to_clipboard):
    string = " ".join(context.args)
    result = ""
    for character in string:
        upper = bool(random.getrandbits(1))
        result += character.upper() if upper else character.lower()
    
    print(result)

    if copy_to_clipboard:
        pyperclip.copy(result)
        print('Copied to clipboard')

if __name__ == '__main__':
    rcase()

sys.modules[__name__] = rcase()