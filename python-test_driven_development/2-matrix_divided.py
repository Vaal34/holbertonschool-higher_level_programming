#!/usr/bin/python3
""" Doc """


def matrix_divided(matrix, div):
    """ divides all elements of a matrix """
    error = ("matrix must be a matrix (list of lists) of integers/floats")
    ref_size = len(matrix[0])
    matrix_matrix = []
    for i in matrix:
        valeur_matrix = []
        for j in i:
            if type(div) not in [int, float]:
                raise TypeError("div must be a number")
            elif type(j) not in [int, float]:
                raise TypeError(error)
            
            if div is float("inf"):
                valeur_matrix.append(0.0)
            else:
                valeur_matrix.append(round(float(j / div), 2))
        if ref_size != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        matrix_matrix.append(valeur_matrix)
    return matrix_matrix
