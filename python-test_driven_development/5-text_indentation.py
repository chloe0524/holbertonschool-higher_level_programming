#!/usr/bin/python3

"""
Module with a function that prints a text with 2 new lines
after each of these characters: `.`, `?` and `:`.
"""


def text_indentation(text):
    """
    prints a text with 2 new lines
    """

    if type(text) is not (str):
        raise TypeError("text must be a string")

    sentence = ""

    for i in text:
        sentence += i

        if i in [".", "?", ":"]:
            print("{}\n".format(sentence.strip()))
            sentence = ""

    if sentence.strip() != "":
        print("{}".format(sentence.strip()), end="")
