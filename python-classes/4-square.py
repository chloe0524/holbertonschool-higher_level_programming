#!/usr/bin/python3


class Square():
    "define square class for python."

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        "getter methods to get size"
        return self.__size

    @size.setter
    def size(self, value):
        "setter methods to set size of square"
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        "calculate area of square"
        return self.__size**2
