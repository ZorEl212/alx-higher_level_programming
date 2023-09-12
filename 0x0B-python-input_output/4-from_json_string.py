#!/usr/bin/python3

"""Module to deserialize a json"""


from json import loads


def from_json_string(my_str):
    """Return object from json
        args:
            my_str: string to deserialize"""

    return loads(my_str)
