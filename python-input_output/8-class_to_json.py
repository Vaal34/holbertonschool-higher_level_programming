#!/usr/bin/python3
""" Doc """


def class_to_json(obj):
    """ class to json """
    return obj.__dict__


"""
obj.__dict__ renvoie un dictionnaire représentant les attributs de l'objet obj
__dict__ est  un attribut spécial d'un objet en Python
qui contient tous les attributs de cet objet sous forme de dictionnaire.
"""
