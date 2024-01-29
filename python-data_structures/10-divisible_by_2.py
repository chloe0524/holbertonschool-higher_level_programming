#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    if my_list is None:
        return None
    for i in my_list:
        if not i % 2:
            list.append(True)
        else:
            list.append(False)
    return list
