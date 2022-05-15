from validator import Validator
import pytest


@pytest.mark.parametrize("expression , expected", [
    ("2*x", True),
    ("2 ^ x + 2", True),
    ("(( 2 * x + 3 ))", True),
    ("(()))(", False),
    ("((()))", True),
    ("(+++)", True),
    (")", False),
    ("(", False)
])
def test_valid_brackets(expression, expected):
    assert Validator().validBrackets(expression) == expected


@pytest.mark.parametrize("expression , expected", [
    ("2*x", True),
    ("2 ^ x + 2", True),
    ("( 2 * x + 2 ) * 3 + 1", True),
    ("(2 * x + 3 * ) x + 1", False),
    ("x ^ 10 + 3 * (x ^ 15 + 3)", True),
    ("x ^ 10 + 2 * x + ", False),
    ("x ^ 3 ^ 2", True),
    ("x ^ (3 ^ 2)", True),
    ("x + 2 + ", False),
    ("x + 2 - -1", True),
    ("x + 2 - - 1", False),
    ("( ( x + 2 ) * 3 )", True)
])
def test_valid_expression(expression, expected):
    assert Validator().validExpression(expression) == expected


@pytest.mark.parametrize("value , expected", [
    ("2.5", True),
    ("-3232.332", True),
    ("3.3.1", False),
    ("-1", True),
    ("0.00", True)
])
def test_valid_numeric_value(value, expected):
    assert Validator().numericValue(value) == expected


@pytest.mark.parametrize("x_min , x_max , expected", [
    ("12", "13", True),
    (12, "13", True),
    (13, 10, False),
    ("12.2.2", "15", False),
    (12, 12, False)
])
def test_valid_range(x_min, x_max, expected):
    assert Validator().validRange(x_min, x_max) == expected


@pytest.mark.parametrize("expression, x_min, x_max, expected", [
    ("x^2", 2, 3, True),
    ("x ^ 2 + (2 * x + 5 - 3) + 1", 10, 100, True),
    ("x + 1 + ", 1, 5, False),
    ("x", 1, 1, False),
    ("x - -1 + 5", 1, -1, False),
    ("x - -1 + 5", -10, -1, True),
])
def test_valid_input(expression, x_min, x_max, expected):
    assert Validator().validInput(expression, x_min, x_max) == expected
