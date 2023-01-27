#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    number_print = 0
    while i != x:
        try:
            print("{:d}".format(my_list[i]), end='')
            number_print += 1
        except (ValueError, TypeError):
            print("", end='')
        i += 1
    print()
    return number_print
