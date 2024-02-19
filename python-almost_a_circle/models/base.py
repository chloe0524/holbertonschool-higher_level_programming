#!/usr/bin/python3
"""class to make """

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
        """adding the class method json save_to_file"""
        if list_objs is None:
            return []
        new_dict = []

        for object in list_objs:
            new_dict.append(object.to_dictionary())

        jstring = cls.to_json_string(new_dict)
        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding="utf-8") as f:
            return (f.write(jstring))
