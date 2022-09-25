#!/usr/bin/python3
def element_at(my_list, idx):
    idx_count = 0
    if  idx < 0 and idx > len(my_list):
        return None
    for i in my_list:
        if idx_count == idx:
            print("Element at index {:d} is {}".format(idx, i))
        idx_count += 1

