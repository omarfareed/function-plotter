from validator import Validator
import pytest


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
    ("x + 2 - - 1", False)
])
def test_valid_expression(expression, expected):
    assert Validator().validate(expression) == expected
