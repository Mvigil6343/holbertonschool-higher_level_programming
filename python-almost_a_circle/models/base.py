#!/usr/bin/python3
"""the “base” of all other classes in this project"""


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
