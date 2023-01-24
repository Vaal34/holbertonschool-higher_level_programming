#!/usr/bin/python3
def max_integer(my_list=[]):
    # Mon code était si beau =\
    '''
    for i in range(len(my_list) - 1):
        if my_list[0] > my_list[1]:
            my_list.remove(my_list[1])
        else:
            my_list.remove(my_list[0])
    return my_list[0]
    '''
    if not my_list:
        return None
    my_list.sort()
    my_list.reverse()
    return my_list[0]
