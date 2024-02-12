#!/usr/bin/python3
"""a class Student that defines a student by: (based on 10-student.py)"""


class Student:
    """class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method that retrieves a dictionary representation of a Student"""
        if not isinstance(attrs, list):
            return self.__dict__
        else:
            dicti = {}
            for i in attrs:
                if i in self.__dict__:
                    dicti[i] = self.__dict__[i]
            return dicti

    def reload_from_json(self, json):
        """method that replaces all attributes of the Student instance"""
        for k, v in json.items():
            setattr(self, k, v)
