#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    len_argv = len(argv) - 1

    if len_argv == 0:
        print("0 arguments.")
    elif len_argv == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len_argv))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
