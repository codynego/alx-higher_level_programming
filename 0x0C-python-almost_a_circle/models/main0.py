#!/usr/bin/python3

from base import Base
from rectangle import Rectangle
from square import Square


"""r1 = Square(5)
print(r1)
print(r1.size)
r1.size = "10"
print(r1)"""


s1 = Square(5)
print(s1)
print(s1.size)
s1.size = 10
print(s1)
s1.size(9)
print(s1)
try:
    s1.size("9")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
