#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    copied_dict = a_dictionary.copy()

    for key in copied_dict:
        copied_dict[key] = copied_dict[key] * 2

    return copied_dict
