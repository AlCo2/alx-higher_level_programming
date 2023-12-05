#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(len(i)):
            if len(i)-1 != j:
                print("{:d}".format(i[j]), end=' ')
            else:
                print("{:d}".format(i[j]))
