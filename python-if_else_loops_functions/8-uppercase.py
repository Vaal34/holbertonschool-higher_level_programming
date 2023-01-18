#!/usr/bin/env python3
def uppercase(str):
    for i in str:
        if ord(i) >= 65 and ord(i) <= 90 or i >= '0' and i <= '9':
           print ("{}".format(i), end=' ')
        elif ord(i) >= 97 and ord(i) <= 123:
            maj = ord(i) - 32
            print ("{}".format(chr(maj)), end=' ')
    print()
