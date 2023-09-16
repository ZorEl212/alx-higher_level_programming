#!/usr/bin/python3
"""Module for 1-rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getattr for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set value for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getattr for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set value for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of the rectangle"""
        return (self.height * self.width)

    def perimeter(self):
        """Return perimeter of the rectangle"""
        return 2 * (self.height + self.width)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        s = (self.width * "#" + "\n") * (self.height - 1) + (self.width * "#")
        return s

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'
