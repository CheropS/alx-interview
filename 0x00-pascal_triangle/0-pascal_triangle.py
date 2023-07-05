#!/usr/bin/python3
"""
Defines a function that returns a list of lists
of integers that represents the pascal's triangle.
"""


def pascal_triangle(n):
    """create a list of lists of integers
    parameters:
        n [int]:
            the number of rows
    return:
        [list of lists of ints]:
            representing the pascal's triangle
    """
    if type(n) is not int:
        raise TypeError("n must be an integer")
    triangle = []
    if n <= 0:
        return triangle
    for x in range(n):
        arr = []
        for y in range(x+1):
            if y == 0:
                arr.append(1)
            elif y == x:
                arr.append(1)
            else:
                arr.append(triangle[x-1][y-1] + triangle[x-1][y])
        triangle.append(arr)
    return triangle