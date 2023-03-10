#!/usr/bin/python3
""" Doc """


from models.base import Base


class Rectangle(Base):
    """ Class inherite from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value_width):
        if type(value_width) is not int:
            raise TypeError("width must be an integer")
        if value_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = value_width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value_height):
        if type(value_height) is not int:
            raise TypeError("height must be an integer")
        if value_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = value_height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value_x):
        if not isinstance(value_x, int):
            raise TypeError("x must be an integer")
        elif value_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = value_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value_y):
        if not isinstance(value_y, int):
            raise TypeError("y must be an integer")
        elif value_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = value_y

    def area(self):
        """ method area """
        return self.__width * self.__height

    def display(self):
        """ method that display the rectangle """
        for position_y in range(self.__y):
            print(end="\n" if self.__y > 0 else "")
        for hauteur in range(self.__height):
            for position_x in range(self.__x):
                print(end=" ")
            for largeur in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        string = f"[Rectangle] ({self.id}) {self.x}/{self.y}"
        string2 = f" - {self.width}/{self.height}"
        return string + string2

    def update(self, *args, **kwargs):
        """ update func"""

        if len(args) > 0:
            if args:
                # si un args exist id prend a la valeur de args[0]
                self.id = args[0]
            if len(args) > 1:
                # si le 2eme args exist width prend a la valeur de args[1]
                self.__width = args[1]
            if len(args) > 2:
                # si 3eme args exist height prend a la valeur de args[2]
                self.__height = args[2]
            if len(args) > 3:
                # si 4eme args exist x prend a la valeur de args[3]
                self.__x = args[3]
            if len(args) > 4:
                # si 5eme args exist y prend a la valeur de args[4]
                self.__y = args[4]
        else:
            for cle, valeur in kwargs.items():
                setattr(self, cle, valeur)

    def to_dictionary(self):
        """ dictionnaire """
        dico = {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
        return dico
