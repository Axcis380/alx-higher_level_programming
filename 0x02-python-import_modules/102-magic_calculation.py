#!/usr/bin/python3

def magic_calculation(a, b):
    """Performs magical calculations."""
    from magic_calculation_102 import add, sub  # Make sure the module and functions exist.

    if a < b:
        c = add(a, b)  # Using the add function
        for i in range(4, 6):
            c = add(c, i)  # Using the add function again
        return c  # Return the computed value

    else:
        return sub(a, b)  # Using the sub function for the "else" branch
