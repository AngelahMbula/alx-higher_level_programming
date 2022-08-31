#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    temp = []
    for x in matrix:
        temp.append(list(map(lambda x : x * x, x)))
    return (temp)
