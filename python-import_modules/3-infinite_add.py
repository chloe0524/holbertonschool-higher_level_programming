#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    len_argv = len(argv) - 1
    num = 0

    if len_argv == 0:
        print("0")
    elif len_argv == 1:
        print("1")
    else:
        for arg in argv[1:]:
            num += int(arg)
        print(num)
