#!/usr/bin/python3

"""Simple square class"""


class Square:
    """ This is a simple square class"""
    def __init__(self, size=0):
        """init
        args:
            size: size of the square"""
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size
        args:
            value: the new value to set"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif int(value) < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area of the square"""

        return self.__size * self.__size
