#!/usr/bin/python3

''' A class that defines a square '''


class Square:
    '''
        Initialization of instance attributes

        Args:
        size (int): The size of the square
    '''
    def __init__(self, size=0):
        '''
            initialization
        '''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
            Calculates the area of a square

            Return: The current square area
        '''

        return self.__size * self.__size

    @property
    def size(self):
        '''
            retrieve the size of the square

            Return: The size of the square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
            set the size of the square

            Args:
            value (int): the new square size
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
