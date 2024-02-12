#!/usr/bin/python3
"""Function that returns the dictionary description for JSON serialization"""


def class_to_json(obj):
    """from obj to JSON"""
    return obj.__dict__
