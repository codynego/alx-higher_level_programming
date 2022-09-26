#!/usr/bin/python3
def max_integer(my_list=[]):
    max_int = 0
    if not my_list:
        return None
    for i in my_list:
        max_int = i if i > max_int else max_int
    return max_int
