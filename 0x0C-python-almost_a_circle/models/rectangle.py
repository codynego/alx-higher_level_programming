#!/usr/bin/python3
""" A rectangle class """
from models.base import Base


class Rectangle(Base):
    """
    A rectangle class that inherit from the base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        A getter for the private width attribute

        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        A setter for the private width attribute
        Args:
        width (int): The new value of width

        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        A getter for the private height attribute

        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Update the private height attribute
        Args:
        height (int): the new value of (height)
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        A getter for private attribute x

        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        get the value of the private attribute (x)
        Args:
        x (int): the new value of x
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        get the value of the private attribute (y)

        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        update the value of self.__y
        Args:
        y (int): the new value of (y)

        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Return the area of rectangle

        """
        return self.__width * self.__height

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #

        """
        row = self.__width * '#'
        for j in range(self.__x):
            print()
        for i in range(self.__height):
            print(f"{self.__y * ' '}{row}")

    def __str__(self):
        """
        Return a str representation of Rectangle

        """
        return f"[Rectangle] - ({self.id}) - {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        Args:
        *args (tuple): a tuple containg all the
        argument in the following order:

        args(id, width, height, x, y)

        """
        if len(args) != 0:
            self.id, self.__width, self.__height, self.__x, self.__y = args
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of rectangle

        """
        dict_rep = {'id': self.id, 'width': self.__width,
                    'height': self.__height, 'x': self.__x, 'y': self.__y}
        return dict_rep
