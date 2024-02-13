#!/usr/bin/python3
"""module with function for read+print file contents"""


class Student:
    """A class for student infos"""

    def __init__(self, first_name, last_name, age):
        """
        Init a new Student object

        Args:
            first_name(str)
            last_name(str)
            age(int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns the dictionary description with filters

        Args:
            attrs()

        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }

    def reload_from_json(self, json):
        """
        changes attributes of Student

        Args:
            json (dict)
        """
        for attr, value in json.items():
            setattr(self, attr, value)
