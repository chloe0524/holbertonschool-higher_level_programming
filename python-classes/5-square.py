#!/usr/bin/python3


"Creates a Square class to make a square"


class Square():
    "define square class for python."

    def __init__(self, size=0):
        """
        Initialize a square.

        Args:
            size(int): size of the square as
            non-negative int
        """
        self.__size = size

    @property
    def size(self):
        """"
        Getter method to get size

        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set size of square

        Args:
            value(int): size of square as
            non-negative int

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        calculate area of square

        Returns:
            area of square(int)
        """
        return self.__size**2

    def my_print(self):
        if self.size == 0:
            print('')
        else:
            for length in range(self.__size):
                for height in range(self.__size):
                    print("#", end="")
                print()
