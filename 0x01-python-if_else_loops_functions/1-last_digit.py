#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
negative = False
n = 0
if number < 9:
    number *= -1
    negative = True
if negative:
    n = number % 10 * -1
    number *= -1
else:
    n = number % 10
if n > 5:
    print(f"Last digit of {number} is {n} and is greater than 5")
elif n == 0:
    print(f"Last digit of {number} is 0 and is 0")
else:
    print(f"Last digit of {number} is {n} and is less than 6 and not 0")
