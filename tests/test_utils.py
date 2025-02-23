"""
Unit tests for utility functions.
"""

import pytest
from calculator.utils import validate_number, validate_operator

def test_validate_number():
    assert validate_number("5") == 5.0
    assert validate_number("-2.5") == -2.5
    assert validate_number("0") == 0.0
    
    with pytest.raises(ValueError):
        validate_number("abc")
    with pytest.raises(ValueError):
        validate_number("")

def test_validate_operator():
    assert validate_operator("+") == "+"
    assert validate_operator("-") == "-"
    assert validate_operator("*") == "*"
    assert validate_operator("/") == "/"
    
    with pytest.raises(ValueError):
        validate_operator("x")
    with pytest.raises(ValueError):
        validate_operator("") 