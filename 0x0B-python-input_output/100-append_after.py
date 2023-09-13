#!/usr/bin/python3
"""
Inserts a line of text to a file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific string
    Args:
        filename: file to read an append text where needed
        search_String: string to search and insert
        new_string: string to insert after the search string
    """

    import os

    temp_filename = filename + ".tmp"

    with open(filename, "r") as source_file, open(temp_filename, "w") as temp_file:
        for line in source_file:
            temp_file.write(line)

            if search_string in line:
                temp_file.write(new_string + "\n")

    os.rename(temp_filename, filename)
