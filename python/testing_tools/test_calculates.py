from calculates import add, subtract
import pytest

def test_add():
    assert add(4, 5) == 9, "add() should return 9"

def test_subtract():
    assert subtract(4, 5) == -1, "sub() should return -1"

