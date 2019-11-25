# Emojis on the command line

<!-- MarkdownTOC -->

- [Author](#author)
- [Requires](#requires)
- [Python requirements:](#python-requirements)
- [Documentation](#documentation)
- [Installation](#installation)
    * [Easy Way](#easy-way)
    * [Python](#python)
- [Example](#example)

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
mypy 0.740 Optional static typing for Python
├── mypy-extensions >=0.4.0,<0.5.0
├── typed-ast >=1.4.0,<1.5.0
└── typing-extensions >=3.7.4
pytest 3.10.1 pytest: simple powerful testing with Python
├── atomicwrites >=1.0
├── attrs >=17.4.0
├── colorama *
├── more-itertools >=4.0.0
├── pluggy >=0.7
├── py >=1.5.0
├── setuptools *
└── six >=1.10.0
texttable 1.6.2 module for creating simple ASCII tables
```

## Documentation

Link here

## Installation

### Easy Way

Instructions here

### Python

- Create a local directory `mkdir python-applications`
- Create a virtualenv `python3 -m venv emoji`
- Activate the environment `source emoji/bin/activate`
- Download latest version and install `pip install emoji_cmd-1.0-py3-none-any.whl`
- Link binary to somewhere on system path `ln -s $(which emoji) /usr/local/bin/emoji`

Alternatively manually install using pip from `requirements.txt` and `setup.py` from the release `tar.gz`.

## Example

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
