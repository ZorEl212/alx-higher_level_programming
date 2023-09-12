#!/usr/bin/python3

"""Module for converting to serialize an object"""


from json import dumps


def to_json_string(my_obj):
    """Return json format of an object
        args:
            my_obj: Object to serialize"""

    return dumps(my_obj)
