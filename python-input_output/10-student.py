#!/usr/bin/python3
""" My class module """


class Student:
    """ Class Student """

    def __init__(self, first_name, last_name, age):
        """ Initialisation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Convertir la classe en JSON """
        dico = {}
        for i in self.__dict__:
            if attrs is not None:
                if i in attrs:
                    dico[i] = self.__dict__[i]
        return dico
