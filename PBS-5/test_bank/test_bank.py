import pytest
import string
from bank import value

alfabeto = string.ascii_lowercase
def test_hello():
    assert value("Hello") == 0

def test_starts_with_h():
    assert value("hi, guy") == 20

def test_else():
    for i in alfabeto:
        if i != "h":
            assert value("i") == 100