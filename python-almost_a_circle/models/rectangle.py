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
        """method returns area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """display the circle that isn't a circle"""
        print("\n" * self.y, end="")
        for is_it_cercle in range(self.__height):
            print(" " * self.x, end="")
            for no_its_not in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """method to print the rectangle with the character #."""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args):
        """assigns an argument to each attribute"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
