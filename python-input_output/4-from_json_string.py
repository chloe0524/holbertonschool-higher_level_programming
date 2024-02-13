#!/usr/bin/python3
import json
"""function to return object from json string"""


def from_json_string(my_str):
    """Return the JSON string representation of object file"""
    return json.loads(my_str)
