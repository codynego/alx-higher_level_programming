#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for mtrix in matrix:
        temp_list = []
        for j in mtrix:
            temp_list.append(j * j)
        new_matrix.append(temp_list)
    return new_matrix
