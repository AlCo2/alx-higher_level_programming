#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import *
    
    size = len(sys.argv)
    argv = sys.argv
    if size == 4:
        op = argv[2]
        num1 = int(argv[1])
        num2 = int(argv[3])
        if op == '+':
            print("{} + {} = {}".format(num1, num2, add(num1, num2)))
        elif op == '-':
            print("{} - {} = {}".format(num1, num2, sub(num1, num2)))
        elif op == '*':
            print("{} * {} = {}".format(num1, num2, mul(num1, num2)))
        elif op == '/':
            print("{} / {} = {}".format(num1, num2, div(num1, num2)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
        
