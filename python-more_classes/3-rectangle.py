#!/usr/bin/python3
"""This is a module for a rectangle class."""


class Rectangle():
    """This is a class for a rectangle object."""
    pass

    def __init__(self, width=0, height=0):
        """This method constructs the object."""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """This property returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        get width.

        Args:
            value.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """property to retrieve height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        get height.

        Args:
            value.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """method returns area of rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """method returns perimeter of rectangle"""
        if self.__width == 0:
            if self.__height == 0:
                return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """method to print the rectangle with the character #."""
        if self.__width == 0:
            if self.__height == 0:
                return ('')
        return "\n".join(["#" * self.width for _ in range(self.height)])
