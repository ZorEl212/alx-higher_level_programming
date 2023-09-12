#!/usr/bin/python3

"""Read a file and print it's contents"""


def read_file(filename=""):
    """Print Contents of a file
        Args:
            filename: name of the file"""

    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
