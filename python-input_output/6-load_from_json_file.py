#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""


import json


def load_from_json_file(filename):
    """function that creates an object"""
    with open(filename, encoding="utf-8") as Jfile:
        obj = json.load(Jfile)
    return obj
