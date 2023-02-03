#!/usr/bin/python3
""" function divide all elem of a matrix """


a = "matrix must be a matrix (list of lists) of integers/floats"


def matrix_divided(matrix, div):
    """ Random """
    if matrix == [] or not isinstance(matrix, list):
        raise TypeError(a)
    if not isinstance(div, (int, float) or div is None):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    new_baby = []
    for row in matrix:
        new_baby = []
        for element in row:
            try:
                if div == float('inf'):
                    new_baby.append(0.0)
                else:
                    new_baby.append(round(element / div, 2))
            except:
                if not isinstance(element, (int, float)):
                    raise TypeError(a)
        if len(new_baby) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append(new_baby)
    return(new_matrix)
