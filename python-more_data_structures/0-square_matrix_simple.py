#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_matrix = []
    for i in matrix:
        # créer une nouvelle ligne pour la nouvelle matrice
        valeur_matrix = []
        for j in i:
            valeur_matrix.append(j * j)
        # ajouter la nouvelle ligne à la nouvelle matrice
        matrix_matrix.append(valeur_matrix)
    return matrix_matrix
