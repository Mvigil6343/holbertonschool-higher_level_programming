#!/usr/bin/python3
"""the “base” of all other classes in this project"""
import json


class Base:
    """Clas that defines the first attribute for the next classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a JSON representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
