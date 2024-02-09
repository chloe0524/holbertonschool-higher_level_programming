#!/usr/bin/python3
"""
function that prints a square with the character `#`
"""


def print_square(size):
    """
    Print a square with the character `#`.

    Args:
        size (int): The side length of the square (psitive integer).
    """

    if type(size) is not (int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for length in range(0, size):
        for height in range(0, size):
            print("#", end="")
        print()
