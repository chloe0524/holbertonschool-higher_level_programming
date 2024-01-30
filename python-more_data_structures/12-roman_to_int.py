#!/usr/bin/python3


def roman_to_int(roman_string):
    roman_dico = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
      }

    num = 0
    for char in roman_string:
        num += roman_dico[char]
    return num
