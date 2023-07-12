#!/usr/bin/python3

"""Module to load json file and save it as python object"""

from json import load


def load_from_json_file(filename):
    """Load a json file and export it as python object
        args:
            filename: json file name"""

    with open(filename, 'r') as myfile:
        return load(myfile)
