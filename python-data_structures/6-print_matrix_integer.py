#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print("[", end="")
        for i, column in enumerate(row):
            print("{:d}".format(column), end="")
            if i < len(row) - 1:
                print(", ", end="")
        print("]")
