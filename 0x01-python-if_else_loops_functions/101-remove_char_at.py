#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    index = 0
    for i in str:
        index += 1
        if index == n:
            continue
        else:
            new_str = new_str + i
    return new_str
