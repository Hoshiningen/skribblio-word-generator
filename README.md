# Skribblio Random Word Selection

This is a python script that generates a random set of words, based on the words given to it in a `.json` word database. The user is able to specify how many words they want to generate, where the given word count needs to be between 4 and the number of words in the given database.

## Dependencies

The script depends on `jsonschema` to validate word databases passed in as command line arguments. It's a good idea is to install dependencies in a virtual environment:

```bash
pip install virtualenv

virtualenv venv
source venv/Scripts/activate

pip install -r requirements.txt
```

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

Skribblio has certain requirements on the words that are given to it for custom games. The following schema (`database.json`) enforces these requirements on any database loaded into it. No words will be selected if the validation fails.

```json
{
    "$schema": "http://json-schema.org/draft-07/schema",
    "title": "Word Database Schema",

    "type" : "object",
    "properties": {
        "name" : {
            "type" : "string",
            "description": "The name of the word database"
        },
        "words" : {
            "type" : "array",
            "description": "An array of words stored in the database",
            "items" : {
                "type" : "string",
                "minLength": 3,
                "maxLength": 30
            },
            "minItems": 4,
            "uniqueItems": true
        }
    },
    
    "required": ["words"]
}
```

## Example Failing Databases

Too few words:

```json
{
    "$schema": "./database.json",
    "name": "",
    "words": [
        "word1", "word2", "word3"
    ]
}
```

A word in the database is shorter than the minimum length:

```json
{
    "$schema": "./database.json",
    "name": "",
    "words": [
        "word1", "word2", "word3", "a"
    ]
}
```

A word in the database is larger than the maximum length:

```json
{
    "$schema": "./database.json",
    "name": "",
    "words": [
        "word1", "word2", "word3", "areallylongwordthatexceedsthemaxlength"
    ]
}
```

The database contains duplicates:

```json
{
    "$schema": "./database.json",
    "name": "",
    "words": [
        "unique1", "unique2", "duplicate", "duplicate"
    ]
}
```
