#!/usr/bin/python3

"""Read a file"""


def read_file(filename=""):
    """Print Contents of a file
        Args:
            filename: name of the file"""

    with open(filename, encoding='utf-8') as myfile:
        print(myfile.read())
