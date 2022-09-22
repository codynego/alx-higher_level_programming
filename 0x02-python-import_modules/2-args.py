#!/usr/bin/python3
import sys
no_of_args = len(sys.argv) - 1
if no_of_args == 1:
    print("{} argument:".format(no_of_args))
elif no_of_args == 0:
    print("{} argument.".format(no_of_args), end="")
elif no_of_args > 1:
    print("{} arguments:".format(no_of_args))

if no_of_args > 1:
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))



