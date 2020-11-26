import argparse
import json
import os
import random

from jsonschema import validate


DB_SCHEMA = r"./database.json"


class WordDatabase(object):
    """Represents a word database"""

    def __init__(self, database_file):
        if not os.path.isfile(database_file):
            raise argparse.ArgumentTypeError(f"Unabled to load: '{database_file}'!")

        database_schema = {}
        with open(DB_SCHEMA, 'r') as schema:
            database_schema = json.load(schema)

        with open(database_file, 'r') as db:
            self.__dict__ = json.load(db)

        # Ensure the database is well-formed
        validate(self.__dict__, database_schema)


    def __str__(self):
        return self.__dict__["name"]

    def __repr__(self):
        return self.__str__()


def word_count_validator(word_count):
    """A validator to ensure the given word count is in the valid range"""

    count = int(word_count)

    if count < 4:
        raise argparse.ArgumentTypeError(f"The chosen word count '{count}' is smaller than the "
                                         f"minimum required (4).")

    return count


def setup_arguments():
    """Configures the acceptable command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Generates a set of words to be used in the game Skribbl.io")

    parser.add_argument("database", nargs=1, type=WordDatabase,
        help="An absolute or relative path to a .json word database")

    parser.add_argument("-wc", "--word-count", type=word_count_validator,
        help="The number of words to generate")

    return parser


def choose_words(database_words, word_count):
    """Randomly selects words based on the given word count. Returns
    all words in a shuffled order if no word count is specified."""

    if word_count is None:
        words = database_words 
        random.shuffle(words)

        return words

    return random.sample(database_words, word_count)


def main():
    """Main function of the script"""

    parser = setup_arguments()
    args = parser.parse_args()

    # Do the selection thing
    chosen_words = choose_words(args.database[0].words, args.word_count)
    print(', '.join(chosen_words))


if __name__ == "__main__":
    main()