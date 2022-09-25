#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    len_list = len(my_list) - 1
    for i in range(len_list, 0, -1):
        print("{}". format(i))
