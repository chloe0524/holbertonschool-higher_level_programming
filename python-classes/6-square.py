#!/usr/bin/python3


"Creates a Square class to make a square"


class Square():
    "define square class for python."

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square.

        Args:
            size(int): size of the square as
            non-negative int
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method to get position

        Returns:
            position of square as a tuple
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set position of square

        Args:
            value (tuple): position of square as a tuple of 2 non-negative ints

        Raises:
            TypeError: If position is not a tuple of 2 non-negative integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        calculate area of square

        Returns:
            area of square(int)
        """
        return self.__size**2

    def my_print(self):
        """
        Print the square with the '#' character.

        Args:
            Self

        Return:
            Nothing (none)

        """
        if self.size == 0:
            print('')
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.size):
                for _ in range(self.__position[0]):
                    print(" ", end="")
                for _ in range(self.size):
                    print("#", end="")
                print()
