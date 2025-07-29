#https://github.com/pseudo-named/lab10-AB-RT.git
#Partner 1: Andrew Belser
#Partner 2: Rylie Troendle


"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError as error:
        return str(error)


def log(a, b):
    try:
        return math.log(a, b)
    except ValueError as error:
        return str(error)

def exp(a, b):
    return a**b




