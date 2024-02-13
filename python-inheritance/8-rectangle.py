#!/usr/bin/python3

"""
This module defines the `BaseGeometry` class.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    BaseGeometry class.
    """

    def __init__(self, width, height):
        """
        initialize shape

        Ags:
            width(unsigned int)
            height(unsigned int)
        """
        self.integer_validator('height', height)
        self.integer_validator('width', width)

        self.__height = height
        self.__width = width
