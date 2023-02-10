#!/usr/bin/python3
""" Doc """


def write_file(filename="", text=""):
    """ write and open a file """
    with open(filename, 'w', encoding="utf-8") as w:
        w.write(text)

    w.close
    return len(text)
