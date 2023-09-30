#!/usr/bin/python3
"""Module for base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.
        """
        fname = cls.__name__ + ".json"
        with open(fname, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(dicts))
