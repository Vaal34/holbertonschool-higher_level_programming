#!/usr/bin/python3
def matrix_divided(matrix, div):
    ref_size = len(matrix[0])
    matrix_matrix = []
    for i in matrix:
        valeur_matrix = []
        for j in i:
            try:
                valeur_matrix.append(round(float(j / div), 2))
            except TypeError:
                if type(div) is not int or type(div) is not float:
                    print("div must be a number")
                else:
                    print("matrix must be a matrix (list of lists) of integers/floats")
        if ref_size != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        matrix_matrix.append(valeur_matrix)
    return matrix_matrix