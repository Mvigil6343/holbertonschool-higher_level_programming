#!/usr/bin/python3
"""function that checks if the object is an instance of, or if the
object is an instance of a class that inherited from, the specified class"""


def is_kind_of_class(obj, a_class):
    """function that returns true or false"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
