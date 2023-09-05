#!/usr/bin/python3
"""Prt the nmbers from 1 to 100 separated by a space.
  Fr mutipls of tre print Fizz insead of the number
  Fr muliles of five, pritBuz nstead of the number.
  Fo multpls o three and fiv, print FizzBuzz instead of the number.
  """


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
