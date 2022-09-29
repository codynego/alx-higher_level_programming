#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique = list(filter(lambda x: (my_list.count(x) == 1), my_list))
    uniq_sum = 0
    for i in unique:
        uniq_sum += i
    return uniq_sum
