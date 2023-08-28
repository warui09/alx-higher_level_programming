#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        num_printed = 0

        if my_list is None:
            my_list = []

        for i in range(x):
            print("{:d}".format(my_list[i]), end='')
            num_printed += 1
        return num_printed
    except IndexError:
        pass
    finally:
        print()
    return num_printed
