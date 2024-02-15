#!/usr/bin/python3
"""the “base” of all other classes in this project"""
import json
from os.path import exists


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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        lst = []
        with open(cls.__name__ + ".json", 'w', encoding="utf-8") as f:
            if list_objs is None:
                pass
            else:
                for x in list_objs:
                    lst.append(x.to_dictionary())
            f.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """method that returns the list of a JSON string representation"""
        lst = []
        if json_string is None or json_string == []:
            return lst
        else:
            lst = json.loads(json_string)
            return lst

    @classmethod
    def create(cls, **dictionary):
        """method that returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        else:
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """method that returns a list of instances"""
        file_name = f"{cls.__name__}.json"
        if not exists(file_name):
            return []
        with open(file_name, "r", encoding="utf-8") as f:
            dics = cls.from_json_string(f.read())
            return [cls.create(**dictionary) for dictionary in dics]
