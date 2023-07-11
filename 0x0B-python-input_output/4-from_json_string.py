#!/usr/bin/python3

"""Module containing jason-obj function"""


from json import loads


def from_json_string(my_str):
    """Return object from json
        args:
            my_str: string to deserialize"""

    return loads(my_str)
