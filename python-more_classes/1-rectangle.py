#!/usr/bin/python3
"module to make a Rectangle"


class Rectangle():
    "class to draw a rectangle using the Rectangle class"
    pass

    def __init__(self, width=0, height=0):
        """
        initialize rectangle instance

        Args:
            width(int)
            height(int)
        """
        self.width = width
        self.height = height

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
        if value < 0:
            raise ValueError('width must be >= 0')
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
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
