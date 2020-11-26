# Skribblio Word Generator

This is a python script that generates a random set of words, based on the words given to it in a `.json` word database. The user is able to specify how many words they want to generate, where the given word count needs to be between 4 and the number of words in the given database.

## Usage

```
usage: generate.py [-h] [-wc WORD_COUNT] database

Generates a set of words to be used in the game Skribbl.io

positional arguments:
  database              An absolute or relative path to a .json word database

optional arguments:
  -h, --help            show this help message and exit
  -wc WORD_COUNT, --word-count WORD_COUNT
                        The number of words to generate
```

The generated words are written to stdout, so you can pipe to a file if you want:

```bash
python generate.py db.json > words.txt
```

## Word Database Schema

Word database files need to be in the following format in order to be used by the python script. The name is for humans, and the list of words is processed by the script. All words need to be capitalized. Duplicate words are removed (case-sensitive) after loading the database.

```json
{
    "name":,
    "words": []
}
```

## Skribblio Custom Word Requirements

The game as the following requirements on custom words:
- The minimum word count is 4
- The maximum word size is 30

The script forces the database to adhere to these requirements. No words will be generated if there's a violation.