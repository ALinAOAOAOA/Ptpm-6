import sys
sys.path.append("D:/PTPM/PR6/Ptpm-6")  
from calculator import add, subtract, multiply, divide
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (6,7,13),
    (-1,1,0),
    (0,0,0),
    (1.5,2.7,4.2)
])
def test_add(a,b,expected):
    assert add(a,b)==expected

@pytest.mark.parametrize("a,b,expected", [
    (10,5,5),
    (-1,-1,0),
    (0,5,-5)
])
def test_subtract(a,b,expected):
    assert subtract(a,b)==expected

@pytest.mark.parametrize("a,b,expected", [
    (6,7,42),
    (-1,1,-1),
    (0,0,0)
])
def test_multiply(a,b,expected):
    assert multiply(a,b)==expected

@pytest.mark.parametrize("a,b,expected", [
    (10,5,2),
    (7,2,3.5)
])
def test_divide(a,b,expected):
    assert divide(a,b)==expected

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10,0)