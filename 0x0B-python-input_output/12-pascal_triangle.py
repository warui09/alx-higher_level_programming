#!/usr/bin/python3
"""
Returns a list of lists of integers representing the
Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the
    Pascal’s triangle of n:

    Args:
        n: always an integer

    Returns:
        A list of lists of integers representing Pascal's
        triangle of n
    """

    my_list = []

    if n <= 0:
        return my_list

    for i in range(n):
        row = []
        row.append(1)
        if i > 0:
            for j in range(1, len(my_list[i - 1])):
                if j < len(my_list[i - 1]):
                    row.append(my_list[i - 1][j - 1] + my_list[i - 1][j])
            row.append(1)
        my_list.append(row)

    return my_list
