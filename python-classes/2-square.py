#!/usr/bin/python3
"define empty class square for python."


class Square():
    "def private size attribute"
    def __init__(self, size=0):
        "initalize square using pirvate attribute size as args"
        self.__size = size

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    pass
