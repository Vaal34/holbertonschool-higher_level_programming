#!/usr/bin/python3
""" Doc """


def inherits_from(obj, a_class):
    """ Check is subclass """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
