#!/usr/bin/python3
""" Doc """


def print_square(size):
    """ Print Square """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and type(size) is float:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
