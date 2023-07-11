#!/usr/bin/python3

"""Module to save provided args to json"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


args_list = list(argv[1:])
save_to_json_file(args_list, "add_item.json")
