#!/usr/bin/python3
"""class to make """

from models.base import Base


class Rectangle(Base):
    """class to make rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        "property to retrieve width of rectangle"
        return self.__width

    @width.setter
    def width(self, value):
        """
        get width

        Args:
            value
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        "property to retrieve height of rectangle"
        return self.__height

    @height.setter
    def height(self, value):
        """
        get height

        Args:
            value
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        "property to retrieve x(int)"
        return self.__x

    @x.setter
    def x(self, value):
        """
        get x

        Args:
            value
        """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        "property to retrieve x(int)"
        return self.__y

    @y.setter
    def y(self, value):
        """
        get y

        Args:
            value
        """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')

        self.__y = value

    def area(self):
        """method returns area of rectangle."""
        return self.__height * self.__width
