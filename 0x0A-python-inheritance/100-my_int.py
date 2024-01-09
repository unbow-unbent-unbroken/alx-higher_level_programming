#!/usr/bin/python3


class MyInt(int):
    """
    A class representing MyInt, which inherits from int with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Overrides the == operator to invert its behavior.
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """
        Overrides the != operator to invert its behavior.
        """
        return not super().__ne__(other)
