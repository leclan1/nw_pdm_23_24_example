"""

Provides useful math functions and constants.

This script provides functions for mathematical computations, as well as
commonly used mathematical constants for reference in other scripts.

AUTHOR: leclan1
DATE: 2023-09-28

Classes:
    
    n/a
    
Functions:
    
    add(a, b) -> float
    multiply(a, b) -> float
    exponentiate(base, power) -> float
    integer_divide(a, b) -> int

Misc variables:
    
    pi: the ratio of a circle's circumference to its diameter
    e: the base of the natural logarithm
    hbar: Planck's constant divided by 2*pi
    
"""

def add(a, b):
    """Returns the sum of a and b"""
    return(a + b)


def multiply(a, b):
    """Returns the sum of a and b"""
    return(a * b)


def exponentiate(base, power):
    """Returns base raised to the power power"""
    return(base ** power)


def integer_divide(a, b):
    """Returns a / b, rounded down to the nearest integer"""
    return(a // b)

pi = 3.142
e = 2.718
hbar = 6.626e-34/(2*pi)