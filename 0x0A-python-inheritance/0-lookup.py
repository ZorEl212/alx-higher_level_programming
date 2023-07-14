#!/usr/bin/python3

"""Lookup module"""


def lookup(obj):
    """Lookup for all attributes and methods of an object
        args:
            obj: object to lookup"""

    result = []
    for i in dir(obj):
        result.append(i)
    return result
