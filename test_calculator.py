import pytest

from calculator import add,subtract,mul,div

def test_add():
    assert add(2,3)==5 # actual ==expected
def test_sub():
    assert subtract(4,3)==1