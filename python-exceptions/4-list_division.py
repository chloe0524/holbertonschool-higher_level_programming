#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    list_other = []
    try:
        for i in range(list_length):
            res = 0
            try:
                res = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
            except TypeError:
                print("wrong type")
            except IndexError:
                print("out of range")
            finally:
                list_other.append(res)
    finally:
        return list_other
