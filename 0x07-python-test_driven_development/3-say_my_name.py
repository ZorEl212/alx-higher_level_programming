#!/usr/bin/python3
""" Simple Module to print name"""


def say_my_name(first_name, last_name=""):
    """ Print a string with the format:
    'My name is <first name> <last name> '"""

    if isinstance(first_name, str) and isinstance(last_name, str):
        print(f'My name is {first_name} {last_name}')
    elif not isinstance(first_name, str):
        raise ValueError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise ValueError("last_name must be a string")
