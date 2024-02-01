#!/usr/bin/python3
"""Coordinates of a square"""


class Square:
    """a class Square that defines a square by: (based on 5-square.py)"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor method"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple and (value[0] < 0 or value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """method that returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """method that prints in stdout the square with the character #"""
        if self.size == 0:
            print()

        for b in range(self.__position[1]):
            print()
        for x in range(self.__size):
            for a in range(self.__position[0]):
                print(" ", end="")
            for y in range(self.__size):
                print("#", end="")
            print()
