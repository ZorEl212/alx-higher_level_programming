#!/usr/bin/python3

"""Module for a writing to a file"""


def write_file(filename="", text=""):
    """Write a string to a file using utf-8 encoding
        arguments:
                filename: Name of the file
                text: input text"""

    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
