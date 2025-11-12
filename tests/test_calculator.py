import pytest
from app.calculator import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5
<<<<<<< HEAD
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 1) == -1

def test_mul():
    assert mul(4, 3) == 12
    assert mul(-2, 3) == -6

def test_div():
    assert div(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
=======

def test_sub():
    assert sub(5, 3) == 2

def test_mul():
    assert mul(4, 3) == 12

def test_div():
    assert div(10, 2) == 5

def test_div_by_zero():
    with pytest.raises(ValueError):
>>>>>>> 0a06da347926d392404c22a6705d09e93790b92a
        div(1, 0)
