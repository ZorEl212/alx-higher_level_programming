#!/usr/bin/python3

"""Module for print_sqare"""


def print_square(size):
    """Print a square with '#'"""
    if not (isinstance(size, int) or (type(size) == float and size >= 0)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for height in range(int(size)):
        print('#' * int(size))
