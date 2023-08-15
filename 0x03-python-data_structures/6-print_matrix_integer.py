#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in matrix:
            for i, element in enumerate(row):
                if i < len(row) - 1:
                    print("{:d}".format(element), end=" ")
                elif i == len(row) - 1:
                    print("{:d}".format(element))
