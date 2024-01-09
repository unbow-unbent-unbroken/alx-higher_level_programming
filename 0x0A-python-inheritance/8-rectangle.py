#!/usr/bin/python3
"""
Defines a class Rectangle (based on 7-base_geometry.py)
"""


class BaseGeometry:
    """
    This class represent a base geometry
    """
    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")
    def interger_validator(self, name, value):
        """
        Validates the given value.

        Args:
        - name: A string representing the name of the value.
        - value: The value to be validated.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    This class represent a rectangle inheriting from Base Geometry

    Attributes:
    - __width: Private width of the rectangle.
    - __height: Private height of the rectangle.
    """
    def __init__(self, width, height):
