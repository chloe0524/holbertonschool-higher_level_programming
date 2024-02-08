#!/usr/bin/python3
"""
    adds two int together and defining expections

    Args:
        a, b = integers
        b = 98
"""


def add_integer(a, b=98):
    """
    add two ints
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a1 = int(a)
    b1 = int(b)

    return a1 + b1
