#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            maj = ord(i) - 32
        else:
            maj = ord(i)
        print ("{}".format(chr(maj)), end='')
    print()
