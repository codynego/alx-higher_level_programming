#!/usr/bin/python3
""" A square class """
from base import Base
from rectangle import Rectangle


class Square(Rectangle):
    """
    A Square class that inherit from the rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        A getter for the private size attribute

        """
        return self.width

    @size.setter
    def size(self, value):
        """
        A setter for the private width attribute
        Args:
        size (int): The new value of size

        """
        if type(value) != "int":
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a str representation of Square

        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - \
{self.size}"

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        Args:
        *args (tuple): a tuple containg all the
        argument in the following order:

        args(id, width, height, x, y)

        """
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = value
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of Square

        """
        return {'id': self.id, 'size': self.__size, 'x': self.x, 'y': self.y}
