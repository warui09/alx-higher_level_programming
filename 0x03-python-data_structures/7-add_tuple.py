#!/usr/bin/python3

"""Add 0 to tuple

if tuple has less than 2 elements, add 0 where needed
"""


def add_zero(tuple_t=()):
    if not tuple_t:
        new_tuple = (0, 0)
    elif tuple_t[0] is None:
        new_tuple = (0, tuple_t[1])
    else:
        new_tuple = (tuple_t[0], 0)

    return new_tuple


""" Write a function that adds 2 tuples. """


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a = add_zero(tuple_a)
    if len(tuple_b) < 2:
        tuple_b = add_zero(tuple_b)

    c = tuple_a[0] + tuple_b[0]
    d = tuple_a[1] + tuple_b[1]

    return (c, d)
