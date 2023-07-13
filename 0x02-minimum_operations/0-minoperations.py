#!/usr/bin/python3
"""
Method that calculates the fewest number of
operations needed to result in exactly
n H characters in the file.
"""


def countOperations(num):
    """ Returns a list of operations until n H """
    count = 1
    op_list = []
    val = num
    while val != 1:
        count += 1
        if val % count == 0:
            while (val % count == 0 and val != 1):
                val /= count
                op_list.append(count)

    return op_list


def minOperations(n):
    """ Return sum of process until n H """
    if n < 2 or type(n) is not int:
        return 0
    values = countOperations(n)
    return sum(values)