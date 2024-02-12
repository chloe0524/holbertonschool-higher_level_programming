#!/usr/bin/python3
"""function returns list of available attributes and methods of an object"""


def lookup(obj):
    """
    list of available attributes and methods

    Args:
        obj: object to return
    """
    return dir(obj)
