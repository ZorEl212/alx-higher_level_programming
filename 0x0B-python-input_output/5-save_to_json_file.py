#!/usr/bin/python3

"""Module to export object to json"""

from json import dump


def save_to_json_file(my_obj, filename):
    """Save object in json file
        args:
            my_obj: object to be saved
            filename: json file name"""

    with open(filename, 'w') as file:
        dump(my_obj, file)
