#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        row_2 = [x**2 for x in row]
        new_matrix.append(row_2)
    return new_matrix
