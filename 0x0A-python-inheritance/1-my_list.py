#!/usr/bin/python3

"""List Module"""


class MyList(list):
    """Child of list class"""

    def print_sorted(self):
        """Print sorted copy of list (self)"""

        s_list = list(self)
        s_list.sort()
        print(s_list)
