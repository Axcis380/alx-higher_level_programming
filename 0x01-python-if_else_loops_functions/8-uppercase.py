#!/usr/bin/python3
def uppercase(str):
    """Pint a strg in upecase"""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
