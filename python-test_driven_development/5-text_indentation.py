#!/usr/bin/python3
def text_indentation(text):
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
    print()ssghjghj
