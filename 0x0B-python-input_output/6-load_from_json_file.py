#!/usr/bin/python3

"""Module to load json file and save it as python object"""

from json import load


def load_from_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as myfile:
        return load(myfile)
