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
        # Créer un dictionnaire vide
        dico = {}
        # Parcourir les attributs de la classe
        for i in self.__dict__:
            # Si les attributs spécifiques ont été fournis
            if attrs is not None:
                # Si l'attribut actuel est dans la liste des attributs spécifiques
                if i in attrs:
                    # Ajouter l'attribut et sa valeur au dictionnaire
                    dico[i] = self.__dict__[i]
                    return dico
        # Retourner tous les attributs de la classe sous forme de dictionnaire
        return self.__dict__
