#!/usr/bin/python3
"""This module contains a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) to stdout."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
