#!/usr/bin/python3

"""Module for base class"""


class Base:
    """Class Base:
        Base class throughout this project

        Private class attribs:
        __nb_objects: Number of instances created"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init method for the class
        args:
            id: identfier for an instance
            """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
