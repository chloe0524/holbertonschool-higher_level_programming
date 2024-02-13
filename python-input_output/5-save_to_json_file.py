#!/usr/bin/python3
"""module with function to append string to file"""

import json


def save_to_json_file(my_obj, filename):
    """Save the JSON string representation of object to file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
