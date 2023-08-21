"""
Add Action Module

Adds two numbers together

Functions:
    1. run(input): Adds two numbers together

Author: Ian Jackson
"""


def run(input):
    """
    Adds two numbers together

    Parameters:
        input (string): The function parameter(s) as a string

    Returns:
        int: The sum of a and b

    """
    paramList = input.split(",")
    a = paramList[0].strip()
    b = paramList[1].strip()
    return int(a) + int(b)
