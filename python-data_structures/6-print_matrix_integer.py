#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for vertical in matrix:
        x = 0
        for horizontal in vertical:
            # x incrémente a chaque tour de bcl pour pas print un esp a la fin
            x += 1
            if x is len(vertical):
                print("{:d}".format(horizontal), end="")
            else:
                print("{:d}".format(horizontal), end=" ")
        print()
