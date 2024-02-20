#!/usr/bin/python3
"""class to make base """

import json


class Base():
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns string rep of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """list of objects to a JSON file"""
        if list_objs is None:
            list_objs = []
        new_dictionary = []

        for object in list_objs:
            new_dictionary.append(object.to_dictionary())

        json_string = cls.to_json_string(new_dictionary)
        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding="utf-8") as file:
            return (file.write(json_string))

    def from_json_string(json_string):
        """ returns the list of the json string rep"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(dictionary['size'])
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load objects from a JSON file and return a list of objects."""
        file_name = cls.__name__ + ".json"
        objects = []

        try:
            with open(file_name, "r") as file:
                data = file.read()
                if data:
                    list_dicts = cls.from_json_string(data)
                    for obj_dict in list_dicts:
                        objects.append(cls.create(**obj_dict))
        except FileNotFoundError:
            pass

        return objects
