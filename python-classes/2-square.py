#!/usr/bin/python3
"""Size validation"""


class Square:
    """a class Square that defines a square by: (based on 1-square.py)"""
    def __init__(self, size=0):
        """Constructor method"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
