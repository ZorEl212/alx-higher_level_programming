#!/usr/bin/python3

"""Module containing obj-jason function"""


from json import dumps


def to_json_string(my_obj):
    """Return json format of an object
        args:
            my_obj: Object to serialize"""

    return dumps(my_obj)
