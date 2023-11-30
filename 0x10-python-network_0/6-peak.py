#!/usr/bin/python3
"""Finds the peak in a list of integers"""

def find_peak(list_of_integers):
    """Returns the peak in a list of integers"""
    if not list_of_integers:
        return None

    for i in range(len(list_of_integers) - 1):
        if i == 0:
            previous = None
        else:
            previous = list_of_integers[i - 1]

        current = list_of_integers[i]

        if i == len(list_of_integers) - 1:
            next_int = None
        else:
            next_int = list_of_integers[i + 1]

        if (previous and current > previous) and (next_int and current > next_int):
            return current
        

        if (previous and current < previous) and (next_int and current > next_int):
            return previous
        """

        if (previous and current > previous) and (next_int and current < next_int):
            return next_int
        """
        if (previous and current == previous) and (next_int and current == next_int):
            return current
