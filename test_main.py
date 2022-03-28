import divisibility

def test_divby5():
    a = 10
    out1 = divisibility.divby5(a)
    assert out1 == True


def test_divby5_1():
    a = 14
    out1 = divisibility.divby5(a)
    assert out1 == False


def test_divby7():
    a = 10
    out1 = divisibility.divby7(a)
    assert out1 == False


def test_divby7_1():
    a = 14
    out1 = divisibility.divby7(a)
    assert out1 == True


def test_divby9():
    a = 10
    out1 = divisibility.divby9(a)
    assert out1 == False


def test_divby9_1():
    a = 18
    out1 = divisibility.divby9(a)
    assert out1 == True


def test_divby11():
    a = 10
    out1 = divisibility.divby11(a)
    assert out1 == False


def test_divby11_1():
    a = 121
    out1 = divisibility.divby11(a)
    assert out1 == True