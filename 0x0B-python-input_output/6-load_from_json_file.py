#!/usr/bin/python3

"""Module for loading json file to an object"""

from json import load


def load_from_json_file(filename):
    """Load a json file and export it as python object
        args:
            filename: json file name"""

    with open(filename, 'r') as file:
        return load(file)
