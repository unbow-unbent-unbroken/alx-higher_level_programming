#!/usr/bin/python3
"""This module contains a function that returns JSON representation"""
import json


def to_json_string(my_obj):
    """Return JSON representation of an object (string)."""
    return json.dumps(my_obj)
