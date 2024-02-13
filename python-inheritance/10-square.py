#!/usr/bin/python3

"""
This module defines the `BaseGeometry` class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    BaseGeometry class.
    """

    def __init__(self, size):
        """
        initialize shape

        Ags:
            width(unsigned int)
            height(unsigned int)
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Calculate area of rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return (self.__size * self.__size)
