#!/usr/bin/python3
"""
Inherits from int
"""


class MyInt(int):
    """
    Inherits from int however == and != are swapped
    """

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
