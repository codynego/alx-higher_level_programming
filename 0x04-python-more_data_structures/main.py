#!/usr/bin/python3

search_replace= __import__('1-search_replace').search_replace

my_list = [1,2,3,3,7]
new_list = search_replace(my_list, 3, 89)
print(new_list)
