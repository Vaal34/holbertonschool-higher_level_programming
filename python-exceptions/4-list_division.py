#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        for i in range(list_length):
            try:
                my_list_1[i] /= my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
                my_list_1[i] = 0
            except TypeError:
                print("wrong type")
                my_list_1[i] = 0
            except IndexError:
                print("out of range")
    finally:
        return my_list_1
