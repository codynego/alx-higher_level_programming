#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(0, len(i) -1):
            print("{}".format(i[j]),end=" ")
        print("{}".format(i[j + 1]))
