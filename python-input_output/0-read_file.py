#!/usr/bin/python3
"""module with function to read file"""


def read_file(filename=""):
    """method to read file with filename"""
    with open(filename, "r") as my_file:
        print(my_file.read())
