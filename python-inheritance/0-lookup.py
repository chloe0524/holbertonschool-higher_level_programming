#!/usr/bin/python3
"""
modules define a function that returns list of available
attributes and methods of an object
"""


def lookup(obj):
    """
    list of available attributes and methods

    Args:
        obj: object to return

    Returns:
        list object
    """
    return dir(obj)
