#!/usr/bin/python3
"""
Module Documentation: This module containsa a function that add two integers.
"""

def add_integer(a, b=98):
    """
    Returns the addition of two integers.

    Args:
        a: (int or float) The first number.
        b: (int or float, optional) The second number defaults to 98.

    Return:
        The sum of two numbers.

    Raises:
        TypeError: if a and b is not an integer or float.
    """
    if type (a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type (b) not in [int, float]:
        raise TypeError("b must be an integer")
    """casting a and b to int if float"""
    a = int(a)
    b = int(b)
    """return the sum"""
    return (a + b)
