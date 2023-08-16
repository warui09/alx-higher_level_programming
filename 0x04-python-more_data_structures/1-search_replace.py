#!/usr/bin/python3


def search_replace(my_list, search, replace):
    def replace_item(x):
        if x == search:
            return replace
        return x

    return list(map(replace_item, my_list))
