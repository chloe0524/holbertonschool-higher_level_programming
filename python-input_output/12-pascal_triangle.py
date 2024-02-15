#!/usr/bin/python3
"""Pascal's triangle task 12"""


def pascal_triangle(n):
    """
    gives list of lists of ints
    representing the Pascal’s triangle

    Args:
        n(int)

    Returns:
        Pascal's Triangle
    """
    if n > 0:
        l_pascal = [[1]]
        for i in range(n - 1):
            my_list = [1]
            if i > 0:
                n = len(l_pascal)
                for j in range(n - 1):
                    my_list.append(l_pascal[i][j] + l_pascal[i][j + 1])
            my_list.append(1)
            l_pascal.append(my_list)
        return l_pascal
    return []
