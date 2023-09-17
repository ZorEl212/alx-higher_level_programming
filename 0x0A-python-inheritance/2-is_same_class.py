#!/usr/bin/python3
"""Module for checking class instance"""


def is_same_class(obj, a_class):
    """Check if an obj is instance of a class"""
    if (isinstance(obj, a_class)):
        return True
    else:
        return False
