#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    a_keys = sorted(list(a_dictionary.keys()))
    sorted_dictionary = dict(sorted(a_dictionary.items()))

    for i in sorted_dictionary:
        print("{}: {}".format(i, sorted_dictionary[i]))
