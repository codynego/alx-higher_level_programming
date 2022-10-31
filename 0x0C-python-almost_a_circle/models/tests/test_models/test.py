#!/usr/bin/python3

from ..models.square import Square
from ..models.rectangle import Rectangle
from ..models.base import Base

r1 = Rectangle(4,7,8,1)
r2 = Rectangle(2, 4)
list_rectangles_input = [r1, r2]
Rectangle.save_to_file(list_rectangles_input)
list_rectangles_output = Rectangle.load_from_file()

for rect in list_rectangles_input:
    print("[{}] {}".format(id(rect), rect))
print("________")

for rect in list_rectangles_output:
    print("[{}] {}".format(id(rect), rect))
"""r2 = Rectangle(3,4)
r3 = Rectangle(1,2)
Rectangle.save_to_file([r1, r2, r3])

with open("Rectangle.json", "r") as file:
    print(file.read())"""

