#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        number_print = 0
        i = 0
        while i != x:
            print(f"{my_list[i]}", end='')
            i += 1
            number_print += 1
        print()
        return number_print
    except IndexError:
        print()
        return x
