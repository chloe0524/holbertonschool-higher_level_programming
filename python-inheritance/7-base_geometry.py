#!/usr/bin/python3

"""
This module defines the `BaseGeometry` class.
"""


class BaseGeometry:
    """
    BaseGeometry class.
    """
    def area(self):
        """method raises 'Exception'"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        check type if int

        Args:
            name(str)
            value(int)
        """
        if type(value) is not (int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
