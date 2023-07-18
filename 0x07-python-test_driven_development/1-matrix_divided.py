#!/usr/bin/python3

"""Module to devide a matrix elements with a constant"""


def matrix_divided(matrix, div):
    """divide a metrix with a constant
        args:
            matrix: matrix to be divided
            div: divisor constant"""

    if (not isinstance(div, (int, float))):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list)):
        raise ValueError("Please input valid matrix")

    for i in matrix:
        if (len(matrix[0]) != len(i)):
            raise ValueError("Each row of the matrix must have the same size")
        for j in i:
            e = "matrix must be a matrix (list of lists) of integers/floats"
            if (not isinstance(j, (int, float))):
                raise TypeError(e)
            elif (float(j) == float('inf')):
                raise OverflowError("Too large number")

    result = list(matrix)
    for i in range(len(result)):
        for j in range(len(result[i])):
            result[i][j] = round(result[i][j]/div, 2)
    return result
