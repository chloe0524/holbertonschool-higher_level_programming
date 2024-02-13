#!/usr/bin/python3
"""module with function to append string to file"""

import json

def to_json_string(my_obj):
    """Return the JSON string representation of object"""
    return (json.dumps(my_obj))
