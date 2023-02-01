#!/usr/bin/python3
def matrix_divided(matrix, div):
    matrix_matrix = []
    try:
        for i in matrix:
            valeur_matrix = []
            for j in i:
                try:
                    valeur_matrix.append(round(float(j / div), 2))
                except ZeroDivisionError:
                    print("division by zero")
                except TypeError:
                    if type(div) is not int:
                        print("div must be a number")
                    else:
                        print("matrix must be a matrix (list of lists) of integers/floats")
            matrix_matrix.append(valeur_matrix)
    except TypeError:
        print("Each row of the matrix must have the same size")
    
    return matrix_matrix