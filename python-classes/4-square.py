#!/usr/bin/python3
""" empty class Square that defines a square """


class Square:
    """ empty class Square that defines a square """

    def __init__(self, size=0):
        """Private instance attribute"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def size(self):
        return self.__size
    
    def size(self, value):
        self.size = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
    

