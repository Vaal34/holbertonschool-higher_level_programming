#!/usr/bin/python3
""" empty class Square that defines a square """


class Square:
    """ empty class Square that defines a square """

    def __init__(self, size=0, position=(0, 0)):
        """Private instance attribute"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter instance"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter instance"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """print square"""
        if self.__size == 0:
            return print()
        for underscore in range(self.__position[1]):
            print(end="\n" if self.__position[1] > 0 else "")
        for i in range(self.__size):
            for underscore in range(self.__position[0]):
                print(end=" ")
            for j in range(self.__size):
                print('#', end='')
            print()
