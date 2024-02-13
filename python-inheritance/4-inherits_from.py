#!/usr/bin/python3

"""
MODULE WITH FUNCTION TO CHECK IF OBJECT IS INSTANCE OF CLASS
"""


def is_same_class(obj, a_class):

    """
    CHECKS IF OBJECT IS INSTANCE OF SPECIFIED CLASS

    ARGS:
        OBJ: ITS AN OBJECT
        A_CLASS: IT HAPPENS TO BE A CLASS

    RETURNS:
        `TRUE` IF OBJECT IS AN EXACT INSTANCE OF THE SPECIFIED CLASS,
        `FALSE` OTHERWISE.
    """
    return (type(obj) is a_class)


def is_kind_of_class(obj, a_class):

    """
    CHECKS IF OBJECT IS INSTANCE OF SPECIFIED CLASS

    ARGS:
        OBJ: ITS AN OBJECT
        A_CLASS: IT HAPPENS TO BE A CLASS

    RETURNS:
        `TRUE` IF OBJECT IS AN EXACT INSTANCE OF THE SPECIFIED CLASS,
        `FALSE` OTHERWISE.
    """
    return isinstance(obj, a_class)


def inherits_from(obj, a_class):

    """
    CHECKS IF OBJECT IS INSTANCE OF CLASS THAT INHERITED

    ARGS:
        OBJ: ITS AN OBJECT
        A_CLASS: IT HAPPENS TO BE A CLASS

    RETURNS:
        `TRUE` IF OBJECT IS AN EXACT INSTANCE OF THE SPECIFIED CLASS,
        `FALSE` OTHERWISE.
    """
    return (isinstance(obj, a_class), type(obj) is a_class)
