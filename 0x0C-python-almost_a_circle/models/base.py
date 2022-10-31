#!/usr/bin/python3

""" A base class """


class Base:

    """ The base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            initializing the instance attributes
            Args:
            id (int): object id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

