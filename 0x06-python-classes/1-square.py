#!/usr/bin/python3

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
