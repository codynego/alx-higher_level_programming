#!/usr/bin/python3

from base import Base
from rectangle import Rectangle

b1 = Rectangle(10, 7, 2, 8)
dictionary = b1.to_dictionary()
json_dictionary = Base.to_json_string([dictionary])
print(dictionary)
print(type(dictionary))
print(json_dictionary)
print(type(json_dictionary))
