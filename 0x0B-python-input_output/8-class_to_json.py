#!/usr/bin/python3

"""Class to json"""


def class_to_json(obj):
    """"Function to return dict description
        Args:
            obj: object """

    return obj.__dict__
