import argparse
import json
import os
import random


class WordDatabase(object):
    """Represents a word database"""

    def __init__(self, database_file):
        if not os.path.isfile(database_file):
            raise argparse.ArgumentTypeError(f"Unabled to load: '{database_file}'!")

        with open(database_file, 'r') as db:
            self.__dict__ = json.load(db)

    def __str__(self):
        return self.__dict__["name"]

    def __repr__(self):
        return self.__str__()


def word_count_validator(word_count):
    """A validator to ensure the given word count is in the valid range [4, inf)"""

    count = int(word_count)

    if count < 4:
        raise argparse.ArgumentTypeError(f"The valid range of word counts is [4, inf)!")

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

    # Remove any duplicate words from the database
    database_words = list(set(args.database[0].words))

    # Verify that the selected word count isn't greater than the number of words in the database
    if args.word_count and len(database_words) < args.word_count:
        raise Exception(f"The number of words you're asking for is greater "
                        f"than the amount contained in the given database! "
                        f"(Desired: {args.word_count}, Given: {len(database_words)})")
    
    # Verify that the length of all words in the database are of acceptable length
    if any(map(lambda word: len(word) > 30, database_words)):
        raise Exception("A word in the given database is larger than 30 characters!")

    chosen_words = choose_words(database_words, args.word_count)
    print(', '.join(chosen_words))


if __name__ == "__main__":
    main()