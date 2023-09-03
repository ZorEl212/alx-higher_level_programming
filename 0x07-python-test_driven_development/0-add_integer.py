#!/usr/bin/python3
""" A simple module for addition function"""


def add_integer(a, b=98):
    """ Add two integers"""

    if type(a) not in [int, float]:
        raise ValueError("a must be an integer")
    elif type(b) not in [int, float]:
        raise ValueError("b must be an integer")
    return int(a) + int(b)
