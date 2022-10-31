#!/usr/bin/python3
""" A square class """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A Square class that inherit from the rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """
        A getter for the private size attribute

        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        A setter for the private width attribute
        Args:
        size (int): The new value of size

        """
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__width = size
        self.__height = size

    def __str__(self):
        """
        Return a str representation of Square

        """
        return f"[Square] - ({self.id}) - {self.x}/{self.y} - \
{self.__size}"

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        Args:
        *args (tuple): a tuple containg all the
        argument in the following order:

        args(id, width, height, x, y)

        """
        if len(args) != 0:
            self.id, self.__size, self.x, self.y = args
            self.width = args[1]
            self.height = args[1]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = value
                    self.__size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of Square

        """
        return {'id': self.id, 'size': self.__size, 'x': self.x, 'y': self.y}
