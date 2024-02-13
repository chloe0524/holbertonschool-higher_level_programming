#!/usr/bin/python3
"""module withfunction for read+print file contents"""

import json


class Student:
    """A class for student infos"""

    def to_json(self):
        """returns the dictionary description"""
        return self.__dict__

    def __init__(self, first_name, last_name, age):
        """Init a new Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
