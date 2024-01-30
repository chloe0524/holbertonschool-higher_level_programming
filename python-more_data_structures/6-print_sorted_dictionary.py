#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    sort_dict = sorted(a_dictionary.items(), key=lambda x: x[0])
    if a_dictionary is not None:
        for key, value in sort_dict:
            print("{} : {}".format(key, value))
