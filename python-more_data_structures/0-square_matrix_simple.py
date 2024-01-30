#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqd_matrix = []
    if matrix:
        for v in matrix:
            sqd_matrix.append(list(map(lambda num: num ** 2, v)))
    return sqd_matrix
