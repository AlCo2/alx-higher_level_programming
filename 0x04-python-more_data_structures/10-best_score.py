#!/usr/bin/python3

def best_score(a_dictionary):
    MAX = 0
    value = ''
    for i in a_dictionary:
        if a_dictionary[i] > MAX:
            MAX = a_dictionary[i]
            value = i
    return value
