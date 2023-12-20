#!/usr/bin/python3

""" A class Square that defines a square by: (based on 0-square.py)."""

class Square:
    """
    Class Square that defines a square by private instance attribute: size.
    """

    def __init__(self, size):
        """
        Initialize a new instance of the Square class.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
