#!/usr/bin/python3
"""module for MyList class"""


class MyList(list):
    """Return sorted list (assending)"""
    def print_sorted(self):
        print(sorted(self))
