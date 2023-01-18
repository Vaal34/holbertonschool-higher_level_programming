#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        der = number % -10 * -1
    else:
        der = number % 10
    print("{}".format(der), end='')
    return der