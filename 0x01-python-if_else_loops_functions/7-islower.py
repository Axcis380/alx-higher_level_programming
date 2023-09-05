#!/usr/bin/python3
# Author: Anas Elbaidouri

def is_lower(c):
    """Function checks for lowercase characters."""
    if 97 <= ord(c) <= 122:
        return True
    else:
        return False
