#!/usr/bin/python3

"""Module for the Base class."""



class Base:
    """The base class for managing id attributes in future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor.

        Args:
            id (int): An integer representing the id. If None, increment
                      __nb_objects and assign the new value to the id attribute.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
