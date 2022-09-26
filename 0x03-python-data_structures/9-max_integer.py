#!/usr/bin/python3
def max_integer(my_list=[]):
    max_int = 0
    if len(my_list) == 0:
        return None
    for i in my_list:
        if int(i) > max_int:
            max_int = int(i)
    return max_int
