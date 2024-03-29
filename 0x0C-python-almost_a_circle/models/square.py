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

    def update(self, *args, **kwargs):
        """Update the Square."""

        arg_names = ["id", "size", "x", "y"]

        if args:
            for i, arg in enumerate(args):
                if i < len(arg_names) and arg is not None:
                    setattr(self, arg_names[i], arg)
            return

        for k, v in kwargs.items():
            if k in arg_names and v is not None:
                setattr(self, k, v)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        return (f'[Square] ({self.id}) {self.x}/{self.y} - '
                f'{self.size}')
