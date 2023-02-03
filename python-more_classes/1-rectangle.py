#!/usr/bin/python3
""" Doc """


class Rectangle:
    """ empty class Square that defines a square """

    def __init__(self, width=0, height=0):
        """Private instance attribute"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter instance"""
        return self.__width

    @height.setter
    def height(self, value):
        """setter instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
