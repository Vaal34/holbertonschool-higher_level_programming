#!/usr/bin/python3
""" Doc """


def append_write(filename="", text=""):
    """ appends a string at the end of a text file """
    with open(filename, 'a', encoding="utf-8") as a:
        new_line = a.write(text)
    return new_line
