#!/usr/bin/python3
"""supplies a function that prints My name is <first name> <last name>"""
def say_my_name(first_name, last_name=""):
    """Attributes
    first_name
        must be a string, otherwise a TypeError exception is raised
    last_name
        must be a string, otherwise a TypeError exception is raised
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
