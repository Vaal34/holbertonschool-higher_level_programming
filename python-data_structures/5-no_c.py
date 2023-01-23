#!/usr/bin/env python3
def no_c(my_string):
    x = ['c', 'C']
    for i in my_string:
        if i is x:
            my_string.remove(i)
    return my_string
