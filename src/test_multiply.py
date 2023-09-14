import multiply


def test_multiply():
    assert multiply.run(2, 3) == 6
    assert multiply.run(0, 1) == 0
    assert multiply.run(-3, 3) == -9

    assert multiply.run("1", "2") == 2
