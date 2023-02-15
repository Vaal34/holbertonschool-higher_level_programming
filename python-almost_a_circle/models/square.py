#!/usr/bin/python3
""" Doc """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Subclass Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialisation """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        string = f"[Square] ({self.id}) {self.x}/{self.y}"
        string2 = f" - {self.height}"
        return string + string2
