#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    divisible_by_2 = True
    for i in my_list:
        if i % 2 == 0:
            new_list.append(divisible_by_2)
        else:
            new_list.append(not divisible_by_2)
    return new_list
