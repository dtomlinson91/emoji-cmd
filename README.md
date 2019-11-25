# Emojis on the command line

<!-- MarkdownTOC -->

- [Author](#author)
- [Requires](#requires)
- [Python requirements:](#python-requirements)
- [Documentation](#documentation)
- [Installation](#installation)
    * [Easy Way](#easy-way)
    * [Python](#python)
        + [From pip](#from-pip)
        + [From local wheel](#from-local-wheel)
        + [From source](#from-source)
- [Example Usage](#example-usage)

<!-- /MarkdownTOC -->


## Author

Daniel Tomlinson <dtomlinson@panaetius.co.uk>

## Requires

`python3.7+`

## Python requirements:

```
argparse 1.4.0 Python command-line parsing library
click 7.0 Composable command line interface toolkit
emojis 0.5.1 Emojis for Python
texttable 1.6.2 module for creating simple ASCII tables
```

## Documentation

[Read the documentation](https://dtomlinson91.github.io/emoji-cmd/)

## Installation

### Easy Way

Run `curl -LSs https://raw.githubusercontent.com/dtomlinson91/emoji-cmd/master/install.sh | bash`

### Python

#### From pip

_coming soon_

#### From local wheel

1. Create a local directory `mkdir python-applications`
1. Create a virtualenv `python3 -m venv emoji`
1. Activate the environment `source emoji/bin/activate`
1. Download latest `.whl` version from [releases](https://github.com/dtomlinson91/emoji-cmd/releases) and install `pip install emoji_cmd-1.0-py3-none-any.whl`
1. Link binary to PATH `ln -s $(which emoji) ~/.local/bin`
1. Deactivate virtualenv `deactivate`

#### From source

1. Follow steps 1-3 above
1. Download `requirements.txt`
1. Download the latest `tar.gz` from [releases](https://github.com/dtomlinson91/emoji-cmd/releases) and extract.
1. Do `pip install -r requirements.txt`
1. Go into the extracted tar folder and do `pip install -e .`
1. Link binary to PATH `ln -s $(which emoji) ~/.local/bin`
1. Deactivate virtualenv `deactivate`

## Example Usage

`emoji --help`

```
Usage: emoji [OPTIONS]

  Emojis on the command line 🥳!

  Search for an emoji with --search EMOJI

Options:
  --help             Show this message and exit.
  --version          Show the version and exit.
  -s, --search TEXT  Prints all emojis matching TEXT
```

`emoji --search cake`

```
I found 5 emojis for cake! 🥳
+-------------+-------+
|  tag/alias  | emoji |
+=============+=======+
| :pancakes:  | 🥞    |
+-------------+-------+
| :fish_cake: | 🍥    |
+-------------+-------+
| :moon_cake: | 🥮    |
+-------------+-------+
| :cake:      | 🍰    |
+-------------+-------+
| :cupcake:   | 🧁    |
+-------------+-------+
```
