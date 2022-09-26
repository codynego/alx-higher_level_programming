#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    j = 0
    for i in matrix:
        for j in range(0, len(i) - 1):
            print("{}".format(i[j]),end=" ")

