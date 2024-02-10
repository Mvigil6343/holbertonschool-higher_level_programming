#!/usr/bin/python3
"""A class called BaseGeometry."""


class BaseGeometry:
    """Empty class BaseGeometry."""

    def area(self):
        """area of BaseGeometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
