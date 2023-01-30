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

    @property
    def size(self):
        """getter instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter instance"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """print square"""
        if self.__size is 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
