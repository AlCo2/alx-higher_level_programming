#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    num1 = 0
    num2 = 0
    for i in range(len(tuple_a)):
        if i == 0:
            num1 += tuple_a[0]
        if i == 1:
            num2 += tuple_a[1]
            break
    for i in range(len(tuple_b)):
        if i == 0:
            num1 += tuple_b[0]
        if i == 1:
            num2 += tuple_b[1]
            break
    return (num1, num2)
