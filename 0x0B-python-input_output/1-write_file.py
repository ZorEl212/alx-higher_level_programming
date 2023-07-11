#!/usr/bin/python3

"""Module for a write_file function"""


def write_file(filename="", text=""):
    """Write a string to a file with utf-8 encoding
        arguments:
                filename: Name of the file
                text: text to be writen"""

    with open(filename, 'w', encoding='utf-8') as myfile:
        return myfile.write(text)
