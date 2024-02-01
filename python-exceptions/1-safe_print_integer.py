#!/usr/bin/python3


def safe_print_integer(value):

    try:
        print("{:d}".format(value))
    except Exception as e:
        return (0)  # false
    return (1)  # true
