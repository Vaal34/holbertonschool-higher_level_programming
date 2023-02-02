#!/usr/bin/python3
""" Doc """


def matrix_divided(matrix, div):
    """ divides all elements of a matrix """
    ref_size = len(matrix[0])
    matrix_matrix = []
    for i in matrix:
        valeur_matrix = []
        for j in i:
            try:
                valeur_matrix.append(round(float(j / div), 2))
            except TypeError:
                if type(div) not in [int, float]:
                    raise("div must be a number")
                elif type(j) not in [int, float]:
                    raise("matrix must be a matrix (list of lists) of integers/floats")
        if ref_size != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        matrix_matrix.append(valeur_matrix)
    return matrix_matrix
