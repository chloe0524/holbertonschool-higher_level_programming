#!/usr/bin.python3

"""
Module with unit tests for the `Square` class.
"""

# Import modules.
from io import StringIO
import json
import sys
import unittest
# Import the classes (Base, Rectangle, Square).
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_Square_methods(unittest.TestCase):
    """
    Test cases for the methods of the `Square` class.
    """
    def test_number_of_objects(self):
        """
        Test if `id` of Base is assigned when `__nb_objects` is 0.
        """
        Base.__nb_objects = 0

        square = Square(42)
        self.assertIsNotNone(square.id, 1)

    def test_init(self):
        """
        Test if instance created with `Base` constructor is a `Base` instance.
        """
        Base.__nb_objects = 0

        square = Square(42)
        self.assertIsInstance(square, Square)

    def test_getter_and_setter(self):
        """
        Test getter and setter for width, height, x, and y.
        """
        Base.__nb_objects = 0

        square = Square(42, 4, 2)
        self.assertEqual(square.width, 42)
        self.assertEqual(square.height, 42)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 2)

    def test_errors(self):
        """
        Test various error conditions when setting attributes.
        """
        Base.__nb_objects = 0

        square = Square(42)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.width = "42"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.width = -42
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            square.height = "42"
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            square.height = -42
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.x = "42"
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square.x = -42
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.y = "42"
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square.y = -42

    def test_area(self):
        """
        Test the calculation of the area.
        """
        Base.__nb_objects = 0

        square = Square(42)
        self.assertEqual(square.area(), square.width * square.height)

    def test_display_without_xy(self):
        """
        Test display when x and y are both 0.
        """
        Base.__nb_objects = 0

        square = Square(2, 4, 0, 0)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        square.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "    ##\n    ##\n")

    def test_display_with_xy(self):
        """
        Test display when x and y are greater than 0.
        """
        Base.__nb_objects = 0

        square = Square(2, 4, 2, 2)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        square.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "\n\n    ##\n    ##\n")

    def test_str(self):
        """
        Test the `__str__` method.
        """
        Base.__nb_objects = 0

        square = Square(42, 4, 2)
        string = square.__str__()
        self.assertEqual(string, "[Square] ({}) 4/2 - 42".format(square.id))

    def test_update_args(self):
        """
        Test the `update` method with positional arguments.
        """
        Base.__nb_objects = 0

        square = Square(20, 10, 4, 2)

        square.update(42)
        string = square.__str__()
        self.assertEqual(string, "[Square] ({}) 10/4 - 20".format(square.id))

        square.update(200, 100, 40, 20)
        string = square.__str__()
        self.assertEqual(string, "[Square] ({}) 40/20 - 100".format(square.id))

        square.update(42, 42, 42, 42)
        string = square.__str__()
        self.assertEqual(string, "[Square] ({}) 42/42 - 42".format(square.id))

        square.update(42, 2, 4)
        string = square.__str__()
        self.assertEqual(string, "[Square] ({}) 4/42 - 2".format(square.id))

        square.update(42, 2, 4, 6, 8)
        string = square.__str__()
        self.assertEqual(string, "[Square] ({}) 4/6 - 2".format(square.id))

    def test_update_kwargs(self):
        """
        Test the `update` method with positional arguments.
        """
        Base.__nb_objects = 0

        square = Square(42)

        square.update(height=40)
        string = square.__str__()
        self.assertEqual(string, "[Square] ({}) 0/0 - 42".format(square.id))

        square.update(width=20)
        string = square.__str__()
        self.assertEqual(string, "[Square] ({}) 0/0 - 42".format(square.id))

        square.update(x=8)
        string = square.__str__()
        self.assertEqual(string, "[Square] ({}) 8/0 - 42".format(square.id))

        square.update(y=4)
        string = square.__str__()
        self.assertEqual(string, "[Square] ({}) 8/4 - 42".format(square.id))

        square.update(width=20, height=10, x=4, y=2, id=42)
        string = square.__str__()
        self.assertEqual(string, "[Square] ({}) 4/2 - 42".format(square.id))

    def test_to_dictionary(self):
        """
        Test the `to_dictionary` method.
        """
        Base.__nb_objects = 0

        square = Square(42, 4, 2, 1)
        square_dictionary = square.to_dictionary()
        new_dictionary = {"size": 42, "x": 4, "y": 2, "id": 1}
        self.assertTrue(square_dictionary == new_dictionary)
