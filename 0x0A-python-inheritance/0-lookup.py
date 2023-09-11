#!/usr/bin/python3
"""returns the list of available attributes and methods of an object"""


def lookup(obj):
    """Attributes
    obj
        object whose attributes and methods will be returned as a list
    """
    return dir(obj)
