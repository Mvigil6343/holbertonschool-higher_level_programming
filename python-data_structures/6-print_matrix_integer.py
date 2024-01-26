#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        length = 1
        for n in i:
            if length != len(i):
                print("{:d}".format(n), end=" ")
            else:
                print("{:d}".format(n), end="")
            length += 1
        print()
