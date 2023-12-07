#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result_matrix = [list(map(lambda y: y ** 2, row)) for row in matrix]
    return result_matrix
