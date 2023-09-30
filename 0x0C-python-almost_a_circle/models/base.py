#!/usr/bin/python3
"""Module for base class"""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """Deserialize a json string and return the list.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_inst = cls(1, 1)
            else:
                new_inst = cls(1)
            new_inst.update(**dictionary)
            return new_inst

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        """
        fname = str(cls.__name__) + ".json"
        try:
            with open(fname, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = f"{cls.__name__}.csv"
        fieldnames = cls.get_fieldnames()

        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if list_objs:
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
            else:
                writer.writeheader()

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        """
        filename = f"{cls.__name__}.csv"
        fieldnames = cls.get_fieldnames()

        try:
            with open(filename, "r", newline="") as csvfile:
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                if fieldnames[1] == "size":
                    list_dicts = [dict([k, int(v)]
                                       for k, v in d.items()) for d
                                  in list_dicts]
                else:
                    list_dicts = [dict([k, int(v)]
                                       for k, v in d.items()) for d
                                  in list_dicts][1:]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def get_fieldnames(cls):
        """Get the field names based on the class type."""
        if cls.__name__ == "Rectangle":
            return ["id", "width", "height", "x", "y"]
        else:
            return ["id", "size", "x", "y"]
