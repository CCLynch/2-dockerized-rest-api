import pytest
from my_module.calculations import add, subtract, multiply, divide, power

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-5, -3) == -8

def test_subtract():

    assert subtract(5, 2) == 3
    assert subtract(2, 5) == -3
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0

def test_multiply():

    assert multiply(2, 4) == 8
    assert multiply(3, 0) == 0
    assert multiply(-2, 3) == -6
    assert multiply(-4, -5) == 20

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5
    assert divide(-6, 3) == -2.0
    assert divide(0, 5) == 0.0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero..."):
        divide(10, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(10, 1) == 10
    assert power(2, -1) == 0.5
    assert power(-2, 3) == -8
    assert power(-2, 2) == 4