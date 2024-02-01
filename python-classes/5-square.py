#!/usr/bin/python3
"""Printing a square"""


class Square:
    """a class Square that defines a square by: (based on 4-square.py)"""
    def __init__(self, size=0):
        """Constructor method"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """method that returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """method that prints in stdout the square with the character #"""
        if self.size == 0:
            print()

        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print()
