#!/usr/bin/python3
for i in range(97, 123):
    if i == ord('q') or i == ord('e'):
        continue
    else:
        print("{}".format(chr(i)), end="")
