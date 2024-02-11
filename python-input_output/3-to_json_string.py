#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""


import json


def to_json_string(my_obj):
    """function to turn an object into a string"""
    obj_str = json.dumps(my_obj)
    return obj_str
