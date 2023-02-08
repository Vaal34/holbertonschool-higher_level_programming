#!/usr/bin/python3
""" Doc """


def read_file(filename=""):
    """ open and read file """
    with open(filename, 'r') as text:
        for value in text:
            print(value, end='')
