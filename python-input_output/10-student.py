#!/usr/bin/python3
"""a class Student that defines a student by: (based on 9-student.py)"""


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
