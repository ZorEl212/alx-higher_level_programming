#!/usr/bin/python3

"""Module for integer mul"""


def add_integer(a, b=98):
    """Return sum of integers"""
    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    return int(a + b)