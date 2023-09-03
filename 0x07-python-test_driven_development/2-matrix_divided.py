#!/usr/bin/python3

""" A simple module to divide a metrix with a constant"""


def make_deepcpy(input_list):
    """ Make deep copy of a list """

    if isinstance(input_list, list):
        return [make_deepcpy(item) for item in input_list]
    else:
        return input_list


def matrix_divided(matrix, div):
    """ Divide a matrix with a constant value 'div'"""

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    for row in range(len(matrix)):
        if len(matrix[0]) != len(matrix[row]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in range(len(matrix[row])):
            e = "matrix must be a matrix (list of lists) of integers/floats"
            if type(matrix[row][element]) not in [int, float]:
                raise TypeError(e)

    result = make_deepcpy(matrix)
    for row in range(len(result)):
        for element in range(len(result[row])):
            result[row][element] = round(result[row][element] / div, 2)
    return result
