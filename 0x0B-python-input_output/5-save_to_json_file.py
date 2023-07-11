#!/usr/bin/python3

"""Module to save obj to json file"""

from json import dump


def save_to_json_file(my_obj, filename):
    """Save object in json file
        args:
            my_obj: object to be saved
            filename: json file name"""

    with open(filename, 'w', encoding='utf-8') as myfile:
        dump(my_obj, myfile)
