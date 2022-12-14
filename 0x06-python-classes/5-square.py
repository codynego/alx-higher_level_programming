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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
             calculate the area of the square
             Return: The area of the square
        '''
        return self.__size * self.__size

    def my_print(self):
        '''
            print square to stdout
        '''
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
