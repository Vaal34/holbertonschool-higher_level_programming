#!/usr/bin/python3
""" Doc """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ SubClass Rectangle """

    def __init__(self, size):
        """ initialisation """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area """
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
