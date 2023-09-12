#!/usr/bin/python3
"""reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Attribute
    filename
        file to read and print
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")