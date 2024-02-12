#!/usr/bin/python3
"""module used for geometry"""


class BaseGeometry():
    """empty for now"""

    def __init__(self):
        """initialize shape"""

    def area(self):
        """method to get area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method to test types"""
        if type(value) is not (int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
