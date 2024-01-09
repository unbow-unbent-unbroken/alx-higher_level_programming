#!/usr/bin/python3
"""Inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class to define rectangle using BaseGeomerty
    """

    def __init__(self, width, height):
        """
        initilize a Rectangle
        """
        self.integer_validation("width", width)
        self.integer_validation("height", height)
        self.__width = width
        self.__height = height
