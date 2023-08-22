import add


def test_add(mocker):
    # mocked_add = mocker.patch.object(Slackbot, "add")
    # mocked_add.return_value = 3

    assert add.run("2, 3") == 5
    assert add.run("0, 1") == 1
    assert add.run("-3, 3") == 0
