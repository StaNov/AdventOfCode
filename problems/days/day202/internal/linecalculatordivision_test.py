import pytest

from . import LineCalculatorDivision


@pytest.fixture
def calculator():
    return LineCalculatorDivision()


def test_calculate_two_divisible_numbers(calculator):
    assert calculator.calculate_line("8 2") == 4


def test_calculate_multiple_divisible_numbers(calculator):
    assert calculator.calculate_line("11 23 13 2 17 19 10 31") == 5
