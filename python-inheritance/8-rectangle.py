#!/usr/bin/python3
""" Doc """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ SubClass BaseGeometry """

    def __init__(self, width, height):
        """ Instantiation """
        self.__height = height
        self.__width = width
        self.__width = BaseGeometry.integer_validator(self, "width", width)
        self.__height = BaseGeometry.integer_validator(self, "height", height)
