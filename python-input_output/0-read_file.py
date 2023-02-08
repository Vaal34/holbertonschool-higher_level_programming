#!/usr/bin/python3
""" Doc """

def read_file(filename=""):
    with open('my_file_0.txt', 'r') as text:
        for value in text:
            print(value, end='')
    print()
