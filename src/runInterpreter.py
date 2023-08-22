import interpreter

addInput = """Function name: add
Function parameter: 1, 2
"""


getCommunitiesInput = """Function name: getCommunities
Function parameter: none
"""

multiplyInput = """Function name: multiply
Function parameter: 2, 3
"""

otherInput = """some other input here"""


def testInterpreter():
    response = interpreter.interpret_message(otherInput)
    print("response is")
    print(response)


testInterpreter()
