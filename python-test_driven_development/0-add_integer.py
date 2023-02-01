#!/usr/bin/python3
"""
    My calculation module
"""


def add_integer(a, b=98):
    """ Addition function """
    try:
        result = a + b
        return int(result)
    except TypeError:
        if type(a) is not int:
            return "a must be an integer"
        else:
            return "b must be an integer"
