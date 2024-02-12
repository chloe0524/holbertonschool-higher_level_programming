#!/usr/bin/python3
"""module used for geometry"""


class BaseGeometry():
    """class 'BaseGeometry'"""

    class BaseGeometry:
        """
        This is the 'BaseGeometry class'.

        Methods:
        area(self): raises an exception with a message
        """
        def area(self):

            """method raising exception"""
        raise Exception("area() is not implemented")

        def integer_validator(self, name, value):
            """
            method checking type of args

            Args:
            name(str)
            value(int)
            """
        if type(value) is not (int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
