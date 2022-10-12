#!/usr/bin/python3

''' A class that defines a square '''


class Square:
    '''
        Initialization of instance attributes

        Args:
        size (int): The size of the square
    '''
    def __init__(self, size=0):
        if type(size) is not "int":
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
