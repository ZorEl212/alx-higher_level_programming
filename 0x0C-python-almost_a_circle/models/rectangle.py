#!/usr/bin/python3
"""Module for Rectangle class
    Inheriting from Base"""
from models.base import Base


class Rectangle(Base):
    """Class Rectange: Child class inheriting from base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Magic method to intialize a rectange
        Args:
            width: rectangle width
            height: rectangle height
            x: x value
            y: y value"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """gettr for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """settr for width"""
        self.__width = value

    @property
    def height(self):
        """gettr for height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
