#!/usr/bin/python3
for i in range(122, 96, -1):
    n = i
    if n % 2 == 1:
        n -= 32
    print("{:c}".format(n), end="")
