#!/usr/bin/python3
""" Doc """


def text_indentation(text):
    """ Jump lines if text is [".", "?", ":"] """
    carspecial = False
    if type(text) is not str:
        raise TypeError("text must be a string")
    for value in text:
        if value in [".", "?", ":"]:
            print(value)
            print()
            carspecial = True
        else:
            if carspecial and value == ' ':
                pass
            else:
                carspecial = False
                print(value, end='')
