#!/usr/bin/python3
""" Doc """


def write_file(filename="", text=""):
    """ write et on open a file """
    with open(filename, 'w', encoding="utf-8") as w:
        w.write(text)

    w.close
    return len(text)
