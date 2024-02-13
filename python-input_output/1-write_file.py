#!/usr/bin/python3
"""module with function to write file"""


def write_file(filename="", text=""):
    """method to write file with filename"""
    with open(filename, "w") as write_the_file:
        return write_the_file.write(text)
