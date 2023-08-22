"""
Interpreter Module

Interprets messages and calls the appropriate actions to return to the slackbot

Functions:
    1. parse_message(message): Attempts to parses a message in the expected format
    2. interpret_message(message): Interpret the message and return a response

Authors: Ian Jackson (add, multiply, hi)
Authors: Michael Vlatko (break, nats)
"""
import asyncio
import basic
import serverNats
import startCollectors


def parse_message(message):
    """
    Attempts to parses a message in the expected format:
    Function name: someFunction
    Function parameter: someParameters, maybeMoreThanOne


    Parameters:
        message (string): The message to parse

    Returns:
        (string, string)|(None, None): The function and parameter, or None

    """
    try:
        lines = message.split("\n")

        functionSplit = lines[0].split(":")
        assert functionSplit[0] == "Function name"
        functionSplit[1] = functionSplit[1].strip()
        assert len(functionSplit[1]) > 0
        functionName = functionSplit[1]

        parameterSplit = lines[1].split(":")
        assert parameterSplit[0] == "Function parameter"
        parameterSplit[1] = parameterSplit[1].strip()
        assert len(parameterSplit[1]) > 0
        parameter = parameterSplit[1]

        return (functionName, parameter)

    except Exception as e:
        # Failed to parse message, attempt NLP
        print("Failure to parse message. Attempting NLP")
        return (None, None)


def interpret_message(message):
    """
    Interprets the message and returns a response

    Parameters:
        message (string): The message to interpret

    Returns:
        string|None: The response to return, or None

    """
    (functionName, parameter) = parse_message(message)

    if functionName != None:
        try:
            module = __import__(functionName)
            return asyncio.run(module.run(parameter))
        except Exception as e:
            print(e)
            return "Error calling module"
    else:
        args = message.split()
        if args[0] == "hi":
            return "hello"
        if args[0] == "break":
            pass_msg = basic.basic_interpret(message)
            string_dict = {key: str(value) for key, value in pass_msg.items()}
            print(string_dict)
            return str(string_dict)
        if args[0] == "nats":
            return asyncio.run(serverNats.send_to(message))
        if args[0] == "example":
            return asyncio.run(startCollectors.run(message))

    return None
