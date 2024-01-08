#!/usr/bin/python3
""" this is a unit test learning """


def matrix_divided(matrix, div):
    """function to divid elements of a matrix """

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or matrix == [] or not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    rowSize = len(matrix[0])
    for row in matrix:
        if len(row) != rowSize:
            raise TypeError("Each row of the matrix must have the same size")
        for i, num in enumerate(row):
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
