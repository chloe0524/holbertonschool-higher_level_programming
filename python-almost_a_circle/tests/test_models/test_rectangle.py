#!/usr/bin.python3

"""
Module with unit tests for the `Rectangle` class.
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


class test_Rectangle_methods(unittest.TestCase):
    """
    Test cases for the methods of the `Rectangle` class.
    """
    def test_number_of_objects(self):
        """
        Test if `id` of Base is assigned when `__nb_objects` is 0.
        """
        Base.__nb_objects = 0

        rectangle = Rectangle(20, 10, 4, 2)
        self.assertIsNotNone(rectangle.id, 1)

    def test_init(self):
        """
        Test if instance created with `Base` constructor is a `Base` instance.
        """
        Base.__nb_objects = 0

        rectangle = Rectangle(20, 10, 4, 2)
        self.assertIsInstance(rectangle, Rectangle)

    def test_getter_and_setter(self):
        """
        Test getter and setter for width, height, x, and y.
        """
        Base.__nb_objects = 0

        rectangle = Rectangle(20, 10, 4, 2)
        self.assertEqual(rectangle.width, 20)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 2)

    def test_errors(self):
        """
        Test various error conditions when setting attributes.
        """
        Base.__nb_objects = 0

        rectangle = Rectangle(20, 10, 4, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.width = "20"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle.width = -20
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rectangle.height = "20"
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle.height = -10
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rectangle.x = "4"
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(20, 10, -4, 2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rectangle.y = "2"
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(20, 10, 4, -2)

    def test_area(self):
        """
        Test the calculation of the area.
        """
        Base.__nb_objects = 0

        rectangle = Rectangle(20, 10, 4, 2)
        self.assertEqual(rectangle.area(), rectangle.width * rectangle.height)

    def test_display_without_xy(self):
        """
        Test display when x and y are both 0.
        """
        Base.__nb_objects = 0

        rectangle = Rectangle(2, 4, 0, 0)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        rectangle.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "##\n##\n##\n##\n")

    def test_display_with_xy(self):
        """
        Test display when x and y are greater than 0.
        """
        Base.__nb_objects = 0

        rectangle = Rectangle(2, 4, 2, 2)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        rectangle.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "\n\n  ##\n  ##\n  ##\n  ##\n")

    def test_str(self):
        """
        Test the `__str__` method.
        """
        Base.__nb_objects = 0

        rectangle = Rectangle(20, 10, 4, 2)
        string = rectangle.__str__()
        self.assertEqual(string, "[Rectangle] (21) 4/2 - 20/10")

    def test_update_args(self):
        """
        Test the `update` method with positional arguments.
        """
        Base.__nb_objects = 0

        rectangle = Rectangle(20, 10, 4, 2)

        rectangle.update(42)
        string = rectangle.__str__()
        self.assertEqual(string, "[Rectangle] (42) 4/2 - 20/10")

        rectangle.update(200, 100, 40, 20)
        string = rectangle.__str__()
        self.assertEqual(string, "[Rectangle] (200) 20/2 - 100/40")

        rectangle.update(42, 42, 42, 42)
        string = rectangle.__str__()
        self.assertEqual(string, "[Rectangle] (42) 42/2 - 42/42")

        rectangle.update(42, 2, 4)
        string = rectangle.__str__()
        self.assertEqual(string, "[Rectangle] (42) 42/2 - 2/4")

        rectangle.update(42, 2, 4, 6, 8)
        string = rectangle.__str__()
        self.assertEqual(string, "[Rectangle] (42) 6/8 - 2/4")

    def test_update_kwargs(self):
        """
        Test the `update` method with positional arguments.
        """
        Base.__nb_objects = 0

        rectangle = Rectangle(20, 10, 4, 2, 0)

        rectangle.update(height=40)
        string = rectangle.__str__()
        self.assertEqual(string, "[Rectangle] (0) 4/2 - 20/40")

        rectangle.update(width=20)
        string = rectangle.__str__()
        self.assertEqual(string, "[Rectangle] (0) 4/2 - 20/40")

        rectangle.update(x=8)
        string = rectangle.__str__()
        self.assertEqual(string, "[Rectangle] (0) 8/2 - 20/40")

        rectangle.update(y=4)
        string = rectangle.__str__()
        self.assertEqual(string, "[Rectangle] (0) 8/4 - 20/40")

        rectangle.update(width=20, height=10, x=4, y=2, id=42)
        string = rectangle.__str__()
        self.assertEqual(string, "[Rectangle] (42) 4/2 - 20/10")

    def test_to_dictionary(self):
        """
        Test the `to_dictionary` method.
        """
        Base.__nb_objects = 0

        rectangle = Rectangle(20, 10, 4, 2, 42)
        rectangle_dictionary = rectangle.to_dictionary()
        new_dictionary = {"width": 20, "height": 10, "x": 4, "y": 2, "id": 42}
        self.assertTrue(rectangle_dictionary == new_dictionary)
