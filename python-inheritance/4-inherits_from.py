#!/usr/bin/python3
""" Doc """


def inherits_from(obj, a_class):
    """ Check is subclass """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False


"""
Si "isinstance(obj, a_class)" renvoie "True", cela signifie que "obj"
est une instance de "a_class" ou d'une de ses sous-classes.
Et si "type(obj) is not a_class" renvoie également
"True", cela signifie que "obj" n'est pas un objet
de la classe "a_class" elle-même, mais plutôt une sous-classe de "a_class".
"""
