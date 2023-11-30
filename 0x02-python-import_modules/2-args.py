#!/usr/bin/python3
import sys

if __name__ == '__main__':
    size = len(sys.argv)
    if size < 2:
        print("0 arguments.")
    else:
        if (size-1 == 1):
            print("{} argument:".format(size - 1))
        else:
            print("{} arguments:".format(size - 1))
        for i in range(size - 1):
            print("{}: {}".format(i+1, sys.argv[i + 1]))
