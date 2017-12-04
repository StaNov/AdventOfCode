import pytest

from . import LineCalculatorMinMax


@pytest.fixture
def calculator():
    return LineCalculatorMinMax()


def test_calculate_two_same_numbers(calculator):
    assert calculator.calculate_line("1 1") == 0


def test_calculate_two_different_numbers_descending(calculator):
    assert calculator.calculate_line("5 2") == 3


def test_calculate_two_different_numbers_ascending(calculator):
    assert calculator.calculate_line("1 8") == 7


def test_calculate_multiple_different_numbers(calculator):
    assert calculator.calculate_line("1 8 4 12 2") == 11
