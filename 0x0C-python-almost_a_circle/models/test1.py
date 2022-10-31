#!/usr/bin/python3


from base import Base
from rectangle import Rectangle
from square import Square
"""r1 = Rectangle(2, 3, 2, 2)
r1.display()

print("---")

r2 = Rectangle(3, 2, 1, 0)
r2.display()"""

r1 = Square(5)
print(r1)

r1.update(10)
print(r1)

r1.update(1, 2)
print(r1)

r1.update(1, 2, 3)
print(r1)

r1.update(1, 2, 3, 4)
print(r1)

