#!/usr/bin/python3
""" Doc """


class Rectangle:
    """ empty class Square that defines a square """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Private instance attribute"""
        Rectangle.number_of_instances += 1
        self.height = height
        self.width = width
        Rectangle.print_symbol

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def perimeter(self):
        """returns the current rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """ print rectangle """
        count = 0
        string = ""

        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            count += 1
            for j in range(self.__width):
                string += str(self.print_symbol)
            if count != self.__height:
                string += '\n'
        return string

    def __repr__(self):
        """ repr rectangle """
        rep = f"Rectangle({self.__width}, {self.__height})"
        return rep

    def __del__(self):
        """ del rectangle """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
