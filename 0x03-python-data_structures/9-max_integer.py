#!/usr/bin/python3
def max_integer(my_list=[]):
    max_int = my_list[0]
    if not my_list:
        return None
    else:
        for i in my_list:
            if i > max_int:
                max_int = i
            else:
                continue
    return max_int