#!/usr/bin.python3

"""
Module with unit tests for the `Base` class.
"""

# Import modules.
import json
import unittest
# Import the classes (Base, Rectangle, Square).
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_Base_methods(unittest.TestCase):
    """
    Test cases for the methods of the `Base` class.
    """
    def test_number_of_objects(self):
        """
        Test if `id` of Base is assigned when `__nb_objects` is 0.
        """
        Base.__nb_objects = 0

        base = Base()
        self.assertIsNotNone(base.id, 1)

    def test_init(self):
        """
        Test if instance created with `Base` constructor is a `Base` instance.
        """
        Base.__nb_objects = 0

        base = Base()
        self.assertIsInstance(base, Base)

    def test_init_with_id(self):
        """
        Test if `id` is correctly assigned when a specific `id` is provided.
        """
        Base.__nb_objects = 0

        base = Base(42)
        self.assertEqual(base.id, 42)

    def test_init_without_id(self):
        """
        Test if `id` is assigned when no `id` is provided.
        """
        Base.__nb_objects = 0

        base = Base()
        self.assertIsNotNone(id(base))

    def test_to_json_string(self):
        """
        Test if to_json_string correctly converts
        a list of dictionaries to JSON.
        """
        Base.__nb_objects = 0

        rectangle = Rectangle(20, 10, 4, 2)
        square = Square(20, 10, 4, 2)
        dictionary = [rectangle.to_dictionary(), square.to_dictionary()]
        json_string = json.dumps([dictionary])
        json_list_of_dictionary = rectangle.to_json_string([dictionary])
        self.assertTrue(json_string == json_list_of_dictionary)

    def test_save_to_file(self):
        """
        Test if save_to_file correctly saves a list of objects to a JSON file.
        """
        Base.__nb_objects = 0

        rectangle = Rectangle(20, 10, 4, 2)
        square = Square(20, 10, 4, 2)
        dictionary = [rectangle.to_dictionary(), square.to_dictionary()]
        Rectangle.save_to_file([rectangle, square])
        with open("Rectangle.json", "r") as file:
            json_list_of_dictionary = json.loads(file.read())
        self.assertTrue(dictionary == json_list_of_dictionary)

    def test_from_fson_string(self):
        """
        Test if from_json_string correctly converts
        a JSON string to a list of dictionaries.
        """
        Base.__nb_objects = 0

        list_input = [{"id": 42, "width": 20, "height": 10}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(list_input == list_output)

    def test_create(self):
        """
        Test if create correctly creates an instance
        from a dictionary of attributes.
        """
        Base.__nb_objects = 0

        rectangle = Rectangle(2, 4, 6, 8)
        list_rectangles_inout = rectangle.to_dictionary()
        new_rectangle = Rectangle.create(**list_rectangles_inout)
        self.assertFalse(rectangle is new_rectangle)
        self.assertFalse(rectangle == new_rectangle)

    def test_load_from_file(self):
        """
        Test if load_from_file correctly loads objects
        from a JSON file and creates instances.
        """
        Base.__nb_objects = 0

        # Test with rectangles
        rectangle_1 = Rectangle(2, 4, 6, 8)
        rectangle_2 = Rectangle(8, 6, 4, 2)
        list_rectangles_input = [rectangle_1, rectangle_2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertTrue(type(list_rectangles_output) is list)
        for rectangle in list_rectangles_input:
            self.assertTrue(isinstance(rectangle, Rectangle))
        for rect in list_rectangles_output:
            self.assertTrue(isinstance(rectangle, Rectangle))

        # Test with squares
        square_1 = Square(2, 4, 6, 8)
        square_2 = Square(8, 6, 4, 2)
        list_squares_input = [square_1, square_2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertTrue(type(list_squares_output) is list)
        for square in list_squares_input:
            self.assertTrue(isinstance(square, Square))
        for sqr in list_squares_output:
            self.assertTrue(isinstance(square, Square))
