import pytest

import divisibility
import pytest
@pytest.mark.parametrize("num,output",[(5,True),(2,False),(10,True),(7,False)])
def test_divby5(num,output):
    out1 = divisibility.divby5(num)

    assert out1 == output

@pytest.mark.parametrize("num1,output1",[(14,True),(20,False),(21,True),(22,False)])
def test_divby7(num1,output1):

    out1 = divisibility.divby7(num1)

    assert out1 == output1

@pytest.mark.parametrize("num2,output2",[(18,True),(2,False),(27,True),(7,False)])
def test_divby9(num2,output2):

    out1 = divisibility.divby9(num2)

    assert out1 == output2

@pytest.mark.parametrize("num3,output3",[(22,True),(23,False),(44,True),(46,False)])
def test_divby11(num3,output3):

    out1 = divisibility.divby11(num3)

    assert out1 == output3