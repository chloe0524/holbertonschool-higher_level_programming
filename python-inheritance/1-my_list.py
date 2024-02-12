#!/usr/bin/python3

"""class a subclass of  `list` class."""


class MyList(list):
    """class of list class."""
    def print_sorted(self):
        """print the elements of the list in ascending sort"""
        print(sorted(self))
