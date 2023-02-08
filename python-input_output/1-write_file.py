#!/usr/bin/python3
""" Doc """


def write_file(filename="", text=""):
    """ write et on open a file """
    with open(filename, 'w') as w:
        w.write(text)