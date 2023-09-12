#!/usr/bin/python3
"""writes a string to a text file (UTF8) and returns the number of characters written"""


def write_file(filename="", text=""):
    """Attributes
    filename
        file to write to
    text
        text to write to the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
