#!/usr/bin/python3

def uppercase(str):
    upper = ""
    for char in str:
        num = ord(char)
        if num >= ord('a') and num <= ord('z'):
            upper += chr(num - 32)
        elif num >= ord('A') and num <= ord('Z'):
            upper += char
        else:
            upper += char
    print("{}".format(upper))
