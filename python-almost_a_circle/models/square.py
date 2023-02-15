#!/usr/bin/python3
""" Doc """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Subclass Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialisation """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        string = f"[Square] ({self.id}) {self.x}/{self.y}"
        string2 = f" - {self.height}"
        return string + string2

    def update(self, *args, **kwargs):
        """ update attr"""
        if len(args) > 0:
            if args:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for cle, valeur in kwargs.items():
                setattr(self, cle, valeur)

    def to_dictionary(self):
        """ dictionnaire """
        dico = {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
        return dico
