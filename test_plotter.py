from plotter import Plotter
import pytest


@pytest.mark.parametrize("expression , x , expected", [
    ("2*x", 2, 4),
    ("2 ^ x + 2", 2, 6),
    ("( 2 * x + 2 ) * 3 + 1", 2, 19),
    ("x ^ 3 ^ 2", 3, 3 ** 3 ** 2),
    ("x + 2 - -1", 0.5, 3.5),
    ("x ^ x ^ x * 5", 0.5, 0.5 ** 0.5 ** 0.5 * 5),
    ("(2 * x) + 3 * x + 2 ", 1, 7),
])
def test_valid_expression(expression, x,  expected):
    assert Plotter().evaluate(expression, x) == expected


@pytest.mark.parametrize("expression , x_min , x_max ,expected", [
    ("2 * x + 3", 0, 100, 1),
    ("2 ** x + 4", 1, 1, 0),
    ("( 2 * x + 2 ) * 3 + 1", -10, 10, 1),
    ("(2 * x + 3 * ) x + 1", 0, 10, 0),
    ("x ^ 10 + 3 * (x ^ 15 + 3)", 100, -100, 0),
    ("x ^ 10 + 2 * x + ", -100, -200, 0),
    ("x ^ 3 ^ 2",  2, 3, 1),
    ("x ^ (3 ^ 2)", 2, -1,  0),
])
def test_plot(expression, x_min, x_max, expected):
    valid = 1
    try:
        Plotter().plot(expression, x_min, x_max)
    except:
        valid = 0
    assert valid == expected
