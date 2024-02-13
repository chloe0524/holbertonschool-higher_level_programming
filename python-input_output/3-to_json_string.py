#!/usr/bin/python3
import json
"""module with function to append string to file"""


def to_json_string(my_obj):
    """Return the JSON string representation of object file"""
    return (json.dumps(my_obj))
