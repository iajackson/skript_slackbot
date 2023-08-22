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


def test_interpreter(mocker):
    mocked_add = mocker.patch("add.run")
    mocked_add.return_value = 3
    mocked_add = mocker.patch("add.run")
    mocked_add.return_value = 3
    response = interpreter.interpret_message("add 1 2")
    assert response == 3

    response = interpreter.interpret_message(addInput)
    assert response == 3
