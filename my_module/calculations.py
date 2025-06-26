"""
This is a set of trivial calculations which will be tested in test_calculations.py
"""

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(numerator, denominator):
    if denominator == 0:
        raise ValueError("Cannot divide by zero...")
    return numerator/denominator

def power(base, exponent):
    return base ** exponent