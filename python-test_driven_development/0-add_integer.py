#!/usr/bin/python3

"""
    module adding two int together and defining expections

    Args:
        a, b = integers
    """


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a, b)
