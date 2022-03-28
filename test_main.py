import main

def test_divby5():
    a = 10
    out1 = main.divby5(a)
    assert out1 == True


def test_divby5_1():
    a = 14
    out1 = main.divby5(a)
    assert out1 == False


def test_divby7():
    a = 10
    out1 = main.divby7(a)
    assert out1 == False


def test_divby7_1():
    a = 14
    out1 = main.divby7(a)
    assert out1 == True


def test_divby9():
    a = 10
    out1 = main.divby9(a)
    assert out1 == False


def test_divby9_1():
    a = 18
    out1 = main.divby9(a)
    assert out1 == True


def test_divby11():
    a = 10
    out1 = main.divby11(a)
    assert out1 == False


def test_divby11_1():
    a = 121
    out1 = main.divby11(a)
    assert out1 == True