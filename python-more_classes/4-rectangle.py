#!/usr/bin/python3
"""a Rectangle"""


from typing import Any


class Rectangle:
    """a class Rectangle that defines a Rectangle"""
    def __init__(self, width=0, height=0):
        """Constructor method"""

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """method that returns the area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """method that returns the perimeter of the Rectangle"""
        if self.__width != 0 and self.__height != 0:
            return (self.__width * 2) + (self.__height * 2)
        else:
            return 0

    def __str__(self):
        """method that returns a string of the Rectangle character #"""
        string = ""
        if self.width == 0 or self.height == 0:
            return string

        for x in range(self.__height):
            for y in range(self.__width):
                string += '#'
            string += '\n'
        return string[:-1]

    def __repr__(self):
        """method that that reproduces the object Rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
