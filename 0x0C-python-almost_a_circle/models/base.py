#!/usr/bin/python3

""" A base class """

import json


class Base:
    """ the base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        Args:
        list_dictionaries: list of dictionaries

        """
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return json.dumps([])
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string

        Args:
        json_string (dictionary):  is a string representing a
        list of dictionaries

        """
        if not json_string:
            return json.loads([])
        else:
            json_object = json.loads(json_string)
            return json_object

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        Args:
        list_object: list of instances who inherits of Base

        """
        if list_objs is None:
            return []
        else:
            json_list = []
            for i in range(len(list_objs)):
                obj_dict = cls.to_dictionary(list_objs[i])
                json_list.append(obj_dict)
            json_objs = cls.to_json_string(json_list)

            with open(f"{cls.__name__}.json", "w") as json_file:
                json_file.write(json_objs)

    @classmethod
    def create(cls, **dictionary):
        """
         returns an instance with all attributes already set

         Args:
         **dictionary: keyword arguments to the new instance

         """
        if cls.__name__ == "Rectangle":
            tmp = cls(1, 1)
            if dictionary.get("width") is None:
                raise ValueError("Value of width not assigned")
            if dictionary.get("height") is None:
                raise ValueError("Value of height not assigned")
        else:
            tmp = cls(size=1)
            if dictionary.get("size") is None:
                raise ValueError("Value of size not assigned")
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        list_inst = []
        try:
            with open(f"{cls.__name__}.json", "r") as json_file:
                obj_file = json_file.read()
            dict_objs = cls.from_json_string(obj_file)
            for i in dict_objs:
                new_instance = cls.create(**i)
                list_inst.append(new_instance)
        except Exception:
            return []
        return list_inst
