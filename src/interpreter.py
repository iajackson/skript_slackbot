"""
Interpreter Module

Interprets messages and calls the appropriate actions to return to the slackbot

Functions:
    1. interpret_message(message): Interpret the message and return a response

Author: Ian Jackson
"""

import add  # TODO: figure out how to dynamically load and call module
import multiply
import basic

def interpret_message(message):
    """
    Interprets the message and returns a response

    Parameters:
        message (string): The message to interpret

    Returns:
        string|None: The response to return, or None

    """

    args = message.split()
    if args[0] == "add":
        return add.run(args[1], args[2])
    elif args[0] == "multiply":
        return multiply.run(args[1], args[2])
    elif args[0] == "hi":
        return "hello"
    elif args[0] == "break":
        pass_msg = basic.basic_interpret(message)
        string_dict = {key: str(value) for key, value in pass_msg.items() }
        print(string_dict)
        return str(string_dict)
        
    return None
