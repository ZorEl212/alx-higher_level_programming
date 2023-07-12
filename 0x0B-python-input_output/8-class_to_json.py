#!/usr/bin/python3

"""Class to json Module"""


def class_to_json(obj):
    """"Function to return dictionary description
        Args:
            obj: object """

    return obj.__dict__
