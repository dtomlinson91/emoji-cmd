import emojis  # type: ignore
import argparse
from texttable import Texttable   # type: ignore


def main(emoji: str) -> None:
    """returns an emoji from a string

    Parameters
    ----------
    emoji : str
        a string for the emoji name/tag/description

    Returns
    -------
    None
    """

    t = Texttable()

    searchOne = [y for y in [x for x in emojis.db.get_tags()] if emoji in y]

    emojiResults = []

    emojiResults.append((['tag/alias', 'emoji']))

    for item in searchOne:
        listOne = [x for x in emojis.db.get_emojis_by_tag(item)]
        for i in range(0, len(listOne)):
            emojiResults.append(
                [(listOne[i][0][0]).strip(), (listOne[i][1]).strip()]
            )

    for alias, emojiAlias in zip(
        emojis.db.get_emoji_aliases().keys(),
        emojis.db.get_emoji_aliases().values(),
    ):
        if emoji in alias:
            emojiResults.append([alias.strip(), emojiAlias.strip()])

    t.add_rows(emojiResults)

    if len(emojiResults) - 1 == 0:
        print(f'I found {len(emojiResults)-1} emojis for {emoji}! 😢')
    else:
        print(f'I found {len(emojiResults)-1} emojis for {emoji}! 🥳')
        print(t.draw())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""
    emoji lookup script to be ran on the shell
"""
    )

    parser.add_argument(
        'emoji',
        type=str,
        help=(
            'full path to list of files. leave blank'
            ' to run in current directory. the results will be'
            ' placed in this folder if specified.'
        ),
    )

    args = parser.parse_args()

    emoji = vars(args)['emoji']

    main(emoji)
