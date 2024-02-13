#!/usr/bin/python3
"""function to return object from json string"""

import json


def from_json_string(my_str):
    """Return the JSON string representation of object file"""
    return (json.loads(my_str))
