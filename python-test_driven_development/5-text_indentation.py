#!/usr/bin/python3
def text_indentation(text):
    i = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    while i != len(text):
        if text[i] in ["." , "?", ":"]:
            print(f"{text[i]}")
            i += 1
        else:
            print(f"{text[i]}", end='')
        i += 1