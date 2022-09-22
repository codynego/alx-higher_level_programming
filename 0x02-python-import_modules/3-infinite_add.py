#!/usr/bin/python3
import sys
no_of_args = len(sys.argv)
args_sum = 0

for i in range(1, no_of_args):
    args_sum += int(sys.argv[i])
print("{}".format(args_sum))



