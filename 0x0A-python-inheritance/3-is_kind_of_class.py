#!/usr/bin/python3
"""Module for class checking"""


def is_kind_of_class(obj, a_class):
    """Check if an object blongs to a class
    or inherites from other class"""
    return isinstance(obj, a_class)
