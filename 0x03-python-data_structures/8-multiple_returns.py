#!/usr/bin/python3

"""Returns a tuple with the length of a string and its first character"""


def multiple_returns(sentence):
    length = len(sentence)

    if len(sentence) > 0:
        first = sentence[0]
    else:
        first = None

    return(length, first)
