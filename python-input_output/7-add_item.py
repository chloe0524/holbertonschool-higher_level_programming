#!/usr/bin/python3
"""module with function to append string to file"""

import json
import os
import sys


def save_to_json_file(my_obj, filename):
    """Save the JSON string representation of object to file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """Return the JSON string representation of object file"""
    with open(filename, "r") as file:
        return json.load(file)


file_name = "add_item.json"

if os.path.exists(file_name):
    my_list = load_from_json_file(file_name)
else:
    my_list = []

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, file_name)
