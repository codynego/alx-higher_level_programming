#!/usr/bin/python3

""" A class that defines a rectangle """


class Rectangle:
    """ Defining a class attribute """

    def __init__(self, width=0, height=0):
        """
            Initializing an instance of the class
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
            Retriving the private attribute width
            return: the width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
            Setting the value of width
            Args:
            value (int): the new width
        """

        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Retrieve the value of height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
            Update the value of height

            Args:
            value (int): the new value of height
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Area of rectangle
        """
        return self.__width * self.__height

    def parameter(self):
        """
            Parameter of a rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0

        return (self.width + self.height) * 2
