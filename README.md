# Sarcastic-Text
Randomizes capitalization of a string input. For example, "Hello there!" can become "hElLO thEre!"

<h1> Getting Started </h1>
These instructions will help you get the program running.

<h2> Prerequisites </h2>
Download the "docopt" and "pyperclip" modules in Python 3. <br>
This can be possibly be done with the following commands:

<pre><code>> pip3 install docopt
> pip3 install pyperclip </code></pre>

<h2> Installation </h2>
Simply download the "sarcastic_text_randomizer.py" file and run it with Python 3.
The usage is described in the docstring as follows:

<pre><code>""" Sarcastic Text Randomizer
Usage:
  sarcastic_text_randomizer.py [&ltstring>]
  sarcastic_text_randomizer.py (-h | --help)
  sarcastic_text_randomizer.py --version

Options:
  [&ltstring>]    Any string to be randomly capitalized [default: ""].
  -h --help     Show this screen.
  --version     Show version.

Description:
    Receives a string input and randomizes the capitalization of the letters
    in that string. Automatically copies the string into the clipboard.
"""</code></pre>

<h1> License </h1>
This project is licensed under the MIT License - see the
 <a href="https://github.com/tbone-iii/Sarcastic-Text/blob/master/LICENSE.md"> LICENSE.md </a>
file for details.