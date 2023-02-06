#!/usr/bin/python3
""" Doc """


class MyList(list):
    """ class MyList that inherits from list """
    def print_sorted(self):
        print(sorted(self))
