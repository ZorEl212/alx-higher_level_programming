#!/usr/bin/python3

"""Simple square class"""


class Square:
    """ This is a simple square class"""

    def __init__(self, size=0):
        """init
        args:
            size: size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif int(size) < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculate and return the are of square"""
        return self.__size * self.__size
