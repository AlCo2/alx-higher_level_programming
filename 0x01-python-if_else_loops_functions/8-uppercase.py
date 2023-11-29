#!/usr/bin/python3
def uppercase(str):
    upper = ''
    for char in str:
        n = ord(char)
        if n >= 97:
            upper += chr(n - 32)
        else:
            upper += char
    print("{}".format(upper))
