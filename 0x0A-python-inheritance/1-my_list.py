#!/usr/bin/python3
"""defines a class MyList that inherits from list"""


class MyList(list):
    """list of integers"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        new_list = self.copy()
        new_list.sort()
        print(new_list)
