import math

def test_isGreaterThanOrEqual100():
    number = 101
    assert (number >= 100) == True

def test_sqrt():
    num = 9
    assert math.sqrt(num) == 3

def test_square():
    num = 7
    assert 7 * 7 == 49