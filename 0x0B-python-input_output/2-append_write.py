#!/usr/bin/python3

"""Module for write_append finction"""


def append_write(filename="", text=""):
    """Append a string to a file
        Args:
            filename: name of the file
            text: text to append to the file"""

    with open(filename, 'a', encoding='utf-8') as myfile:
        return myfile.write(text)
