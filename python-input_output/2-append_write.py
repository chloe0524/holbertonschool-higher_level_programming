#!/usr/bin/python3
"""module with function to append string to file"""


def append_write(filename="", text=""):
    """method to append text to file with filename"""
    with open(filename, "a") as add_file:
        return add_file.write(text)
