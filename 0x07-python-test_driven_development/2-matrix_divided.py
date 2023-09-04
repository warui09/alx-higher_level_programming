#!/usr/bin/python3
"""Divides all elements of a matrix and returns a new matrix"""


def matrix_divided(matrix, div):
    """Matrix is a lists of lists of numbers (integers or floats)
    otherwise a TypeError exception is raised with the message:
    'matrix must be a matrix (list of lists) of integers/floats'

    rows of the matrix must be same size otherwise a TypeError
    exception is raised with the message:
    'Each row of the matrix must have the same size'

    div must be a number otherwise a TypeError Exception is raised
    with the message: 'div must be a number'

    div must greater than 0 otherwise a ZeroDivisionError exception
    is raised with the message: 'division by zero'
    """

    list_size = len(matrix[0])
    new_matrix = []

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = []
        if len(row) != list_size:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, int) and not isinstance(element, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
            new_row.append(round((element / div), 2))
        new_matrix.append(new_row)

    return new_matrix
