#!/usr/bin/python3
"""
checks if an object is an instance of a class
or inherited.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of s class that is
    inherited directly or indirectly from the specified class otherwise False.
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
