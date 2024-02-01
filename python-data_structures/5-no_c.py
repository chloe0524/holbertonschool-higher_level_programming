#!/usr/bin/python3

def no_c(my_string):
    new_str = str.maketrans('', '', 'cC')
    return my_string.translate(new_str)
