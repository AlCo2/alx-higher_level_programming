#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0

    r = {'I': 1, 'V': 5, 'X': 10,
         'L': 50, 'C': 100, 'D': 500,
         'M': 1000
         }
    number = 0
    size = len(roman_string)
    for i in range(0, size):
        if i + 1 < size and r[roman_string[i]] < r[roman_string[i + 1]]:
            number += r[roman_string[i + 1]] - r[roman_string[i]]
        else:
            number += r[roman_string[i]]
    return number
