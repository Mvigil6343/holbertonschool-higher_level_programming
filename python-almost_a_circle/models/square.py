#!/usr/bin/python3
"""file that contains the class Square that inherits from Rectangle"""
from .rectangle import Rectangle


class Square(Rectangle):
    """class that builds a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """shows the class name and the attributes"""
        return f"[{type(self).__name__}] ({self.id}) {self.x}\
/{self.y} - {self.width}"
