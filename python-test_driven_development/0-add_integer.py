#!/usr/bin/python3


"""
    function to add two integers
    Args:
        a and b must be int or float
    Return:
        int a + int b
"""


def add_integer(a, b=98):
    """
    adds two ints
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
