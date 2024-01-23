#!/usr/bin/python3

for i in range(8):
    for j in range(i + 1, 10):
        print("{}{}, ".format(i, j), end='')

for i in range(8, 9):
    for j in range(i, 10):
        print("{}{}".format(i, j), end=", ")
print(89)
