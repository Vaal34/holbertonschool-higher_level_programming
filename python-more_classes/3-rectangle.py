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
        return self.__height

    @height.setter
    def height(self, value):
        """setter instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the current rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the current rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """ print rectangle """
        count = 0
        str = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            count += 1
            for j in range(self.__width):
                str += '#'
            if count != self.__height:
                str += '\n'
        return str
