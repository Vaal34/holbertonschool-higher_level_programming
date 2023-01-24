#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        x = 0
        for j in i:
            x += 1
            if x is len(i):
                print("{}".format(j), end="")
            else:
                print("{}".format(j), end=" ")
        print()
