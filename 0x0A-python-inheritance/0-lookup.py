#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    - obj: The object to inspect.

    Returns:
    - A list containing the attributes and methods of the object.
    """
    return dir(obj)

