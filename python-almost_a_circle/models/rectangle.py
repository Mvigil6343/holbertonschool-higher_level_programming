#!/usr/bin/python3
"""File that contains the class Rectangle that inherits from Base"""
from .base import Base


class Rectangle(Base):
    """Class that builds a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """method that prints in stdout the rectangle"""
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            for a in range(self.__y):
                print()
            for x in range(self.__height):
                for a in range(self.__x):
                    print(" ", end="")
                for y in range(self.__width):
                    print("#", end="")
                print()

    def __str__(self):
        """shows the class name and the values"""
        return f"[{type(self).__name__}] ({self.id}) {self.x}\
/{self.y} - {self.width}/{self.height}"
