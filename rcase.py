import sys
import click
import random

settings = dict(
    allow_extra_args=True
)

@click.command(context_settings=settings)
@click.pass_context
def rcase(context):
    string = " ".join(context.args)
    result = ""
    for character in string:
        upper = bool(random.getrandbits(1))
        result += character.upper() if upper else character.lower()
    print(result)

if __name__ == '__main__':
    rcase()

sys.modules[__name__] = rcase()