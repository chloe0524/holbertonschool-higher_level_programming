#!/usr/bin/python3
"""function to return object from json string"""

import json


def load_from_json_file(filename):
    """Return the JSON string representation of object file"""
    with open(filename, "r") as file:
        return json.load(file)
