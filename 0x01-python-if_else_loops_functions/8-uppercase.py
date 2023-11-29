#!/usr/bin/python3
def uppercase(str):
    for char in str:
        n = ord(char)
        if n >= 97:
            print("{}".format(chr(n - 32)), end='')
        else:
            print(char, end='')
