#!/usr/bin/python3
""" Doc """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ SubClass BaseGeometry """

    def __init__(self, width, height):
        """ Instantiation """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
