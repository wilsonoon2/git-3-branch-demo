from src.math_utils import add, divide
import pytest

def test_add():
    assert add(2, 3) == 6
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

