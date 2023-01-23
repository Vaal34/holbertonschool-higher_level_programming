#!/usr/bin/python3
def no_c(my_string):
    new_list = list(my_string)
    for i in new_list:
        if i == 'c':
            new_list.remove('c')
        elif i == 'C':
            new_list.remove('C')
    new_list = "".join(new_list)
    return new_list
