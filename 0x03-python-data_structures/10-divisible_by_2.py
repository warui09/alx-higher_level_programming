#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    result_list = []
    if len(my_list) == 0:
        return result_list
    else:
        for i in my_list:
            result_list.append(i % 2 == 0)

        return result_list
