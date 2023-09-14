"""
Multiply Action Module

Multiplies two numbers together

Functions:
    1. run(a,b): Multiplies two numbers together

Author: Ian Jackson
"""


async def run(input):
    """
    Multiplies two numbers together

    Parameters:
        input (string): The function parameter(s) as a string

    Returns:
        int: The product of a and b

    """
    paramList = input.split(",")
    a = paramList[0].strip()
    b = paramList[1].strip()
    return int(a) * int(b)
