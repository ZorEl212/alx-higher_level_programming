#!/usr/bin/python3
"""Module for Class square
    Inherits from base Class 'Rectangle'"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square with attribs inheriting from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        return (f'[Square] ({self.id}) {self.x}/{self.y} - '
                f'{self.size}')
