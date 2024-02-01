#!/usr/bin/python3
"""Area of a square"""


class Square:
    """a class Square that defines a square by: (based on 2-square.py)"""
    def __init__(self, size=0):
        """Constructor method"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """method that returns the area of the square"""
        self.area = self.__size**2
        return self.area
