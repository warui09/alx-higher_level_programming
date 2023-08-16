#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    a_dict = a_dictionary.copy()
    for i in a_dictionary:
        a_dict.update({i: a_dict[i] * 2})

    return a_dict
