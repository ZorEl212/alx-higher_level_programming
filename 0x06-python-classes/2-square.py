#!/usr/bin/python3

"""Simple square class"""


class Square:
    """Simple square class"""

    def __init__(self, size=0):
        """init
        args:
            size: size of the square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif int(size) < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
