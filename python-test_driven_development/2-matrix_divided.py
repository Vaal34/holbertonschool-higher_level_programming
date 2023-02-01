#!/usr/bin/python3
""" Shebang Module"""

def matrix_divided(matrix, div):
    """ divides all elements of a matrix """ 
    size_ref = len(matrix[0])
    matrix_matrix = []
    try:
        for i in matrix:
            valeur_matrix = []
            for j in i:
                valeur_matrix.append(round(float(j / div), 2))
            if len(i) != size_ref:
                return ("Each row of the matrix must have the same size")
            matrix_matrix.append(valeur_matrix)
        return matrix_matrix
    except TypeError:
        if type(div) is not int:
            print("div must be a number")
        else:
            print("matrix must be a matrix (list of lists) of integers/floats")
