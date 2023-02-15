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
        if len(args) > 0:
            if args:
                self.id = args[0]
            elif len(args) > 2:
                self.size = args[1]
            elif len(args) > 3:
                self.x = args[2]
            elif len(args) > 4:
                self.y = args[3]
        else:
            for cle, valeur in kwargs.items():
                setattr(self, cle, valeur)        
