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

import pyperclip

from docopt import docopt
from random import random


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
        sarcastic_text = string_randomize(string)
        pyperclip.copy(sarcastic_text)
        print(sarcastic_text)
    else:
        string = input('String to randomize: \n')
        sarcastic_text = string_randomize(string)
        pyperclip.copy(sarcastic_text)
        print(sarcastic_text)

    # Hangs the subprocess to avoid closing immediately.
    input()
