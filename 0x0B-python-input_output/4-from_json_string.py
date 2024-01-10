#!/usr/bin/python3
"""This module contain a function that returns an object"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string."""
    return json.loads(my_str)
