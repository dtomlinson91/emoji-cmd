import emoji_cmd
from emoji_cmd.__version__ import __version__
import click
import sys


@click.command()
@click.help_option()
@click.version_option(version=__version__ + ', (Mon Nov 25 02:08:55 2019)')
# @click.argument('emoji')
@click.option(
    '-s', '--search', 'emoji', help='Prints all emojis matching TEXT', type=str
)
def cli(emoji: str):
    """Emojis on the command line 🥳!

    Search for an emoji with --search EMOJI
    """
    emoji_cmd.main(emoji)


if getattr(sys, 'frozen', False):
    cli(sys.argv[1:])

# if __name__ == '__main__':
#     options = '--help'

#     print(f'> ' + options)
#     cli(options.split())
