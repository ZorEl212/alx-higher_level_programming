#!/usr/bin/python3
"""Module for class checking"""


def inherits_from(obj, a_class):
    """Check if an object blongs to a class
    or inherites from other class"""
    if (isinstance(obj, a_class)) and type(obj) != a_class:
        return True
    return False
