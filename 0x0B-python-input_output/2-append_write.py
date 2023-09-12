#!/usr/bin/python3
""" appends a string at the end of a text file (UTF8) and returns
the number of characters added"""


def append_write(filename="", text=""):
    """Attributes
    filename
        file to append text to
    text
        text to append to the specified file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
