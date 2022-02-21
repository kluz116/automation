import test_allan

def test_sum():
    assert test_allan.getSum(2,4)==6

def test_len():
    assert test_allan.lenList([1,2,3,4,5])==5