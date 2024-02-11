#!/usr/bin/python3
"""Define a Rectangle class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        """Constructor method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """method that calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """method that returns a string of the Rectangle"""
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"
