#/usr/bin/python3

""" A class that defines a rectangle """


class Rectangle:
    """ Defining a class attribute """

    def __init__(self, width=0, height=0):
        """ 
            Initializing an instance of the class
        """
        if not isinstance(width, int) or not isinstance(width, float):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int) or not isinstance(height, float):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.width = width
        self.height = height

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

            return: no return
        """
        if not isinstance(value, int) or not isinstance(value, float):
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
    def height(self, height):
        """
            Update the value of height
            Args:
            value (int): the new value of height
        """
        if not isinstance(value, int) or not isinstance(value, float):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
