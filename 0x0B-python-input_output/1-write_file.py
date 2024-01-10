#!/usr/bin/python3
"""
Module Documentation: This module contains a function that writes a string to a text file
    and return the number of characters written.
"""


def write_file(filename="", text=""):
    """Writes a text file (UTF8) to stdout."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        f.close()



