#!/usr/bin/python3
"""This is a module for a rectangle class."""


class Rectangle():
    """This is a class for a rectangle object."""
    pass

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """This method constructs the object."""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """method to print the rectangle with the character #."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join((str(self.print_symbol) * self.width
                          for worst_than_square in range(self.height)))

    def __repr__(self):
        """method returns str representation of the rectangle."""
        return "Rectangle({}, {})".format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        method returns the biggest rectangle based on area.

        Args:
            rect_1: instance of retcangle
            rect_2: instance of retcangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """method returns a new rectangle"""
        return cls(size, size)

    def __del__(self):
        """method deletes object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __del__(self):
        """method deletes object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
