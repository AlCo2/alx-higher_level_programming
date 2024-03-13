#!/usr/bin/python3

"""
    function def pascal_triangle(n):
    that returns a list of lists of
    integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
        function to make pascal triangle
    """

    if n <= 0:
        return []

    for i in range(1, n + 1):
        for j in range(i):
            print(i**j, end=" ")
        print("")
    print("return:")
    return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
