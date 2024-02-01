#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    numerus = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
        except Exception as e:
            break
        numerus += 1
    print()

    return numerus
