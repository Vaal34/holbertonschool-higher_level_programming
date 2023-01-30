#!/usr/bin/python3
""" empty class Square that defines a square """


class Square:
    """ empty class Square that defines a square """

    def __init__(self, size=0):
        """Private instance attribute"""
        try:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            print("size must be an integer")
