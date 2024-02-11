#!/usr/bin/python3
"""function that returns an object represented by a JSON string"""


import json


def from_json_string(my_str):
    """function that turns a json into an object"""
    str_obj = json.loads(my_str)
    return str_obj
