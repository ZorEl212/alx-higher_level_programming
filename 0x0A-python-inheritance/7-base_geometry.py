#!/usr/bin/python3
"""Module for integer validator"""


class BaseGeometry:
    """No area for now"""
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validate an integer"""
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
