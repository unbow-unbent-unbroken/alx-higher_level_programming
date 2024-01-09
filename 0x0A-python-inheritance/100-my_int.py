#!/usr/bin/python3
"""this module defines a class MyInt that inherits from int"""


class MyInt(int):
    """A class representing MyInt, which inherits from int with inverted == and != operators."""

    def __eq__(self, other):
        """Overrides the == operator to invert its behavior."""
        return self.real != other

    def __ne__(self, other):
        """Overrides the != operator to invert its behavior."""
        return self.real == other
