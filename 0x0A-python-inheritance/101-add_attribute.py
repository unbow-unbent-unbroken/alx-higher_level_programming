#!/usr/bin/python3
"""this module defines a function that adds attributes to objects"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible.

    Raises a TypeError exception if the object can't have a new attribute.

    Args:
    - obj: The object to which the attribute should be added.
    - attr: The name of the new attribute.
    - value: The value of the new attribute.
    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
