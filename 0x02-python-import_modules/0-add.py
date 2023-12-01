#!/usr/bin/python3
# Assign values to variables
a = 1
b = 2

# Import the add function from add_0.py
from add_0 import add

# Call the add function with the assigned variables
result = add(a, b)

# Print the result using string formatting
print("{} + {} = {}".format(a, b, result))
