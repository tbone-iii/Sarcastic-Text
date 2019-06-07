""" Sarcastic Text Randomizer
Usage:
  sarcastic_text_randomizer.py [<string>]
  sarcastic_text_randomizer.py (-h | --help)
  sarcastic_text_randomizer.py --version

Options:
  [<string>]    Any string to be randomly capitalized [default: ""].
  -h --help     Show this screen.
  --version     Show version.

"""

from docopt import docopt
from random import random

# Feature(s) to add.
# TODO:
# ! 1) Automatically add the result to the clipboard.


def string_randomize(string: str) -> str:
    """ Takes a string and randomly capitalizes the characters. """

    string = string.lower()
    letter_list = []
    for letter in string:
        # Serves to give a random boolean output (i.e. 0 or 1)
        if round(random()):
            letter_list.append((letter.upper()))
        else:
            letter_list.append((letter))

    return(''.join(letter_list))


if __name__ == "__main__":
    arguments = docopt(__doc__, version='Sarcastic Text Randomizer 1.0')
    string = arguments["<string>"]
    if string:
        print(string_randomize(string))
    else:
        string = input('String to randomize: \n')
        print(string_randomize(string))

    # Hangs the subprocess to avoid closing immediately.
    input()
