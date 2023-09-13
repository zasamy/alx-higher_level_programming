#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """returns a list of lists of int to represent pascal's triangle"""
    if n <= 0:
        return []
    pascal = [[1]]
    while len(pascal) != n:
        a = pascal[-1]
        b = [1]
        for i in range(len(a) - 1):
            b.append(a[i] + a[i+1])
        b.append(1)
        pascal.append(b)
    return pascal
