import pytest

from . import LineCalculatorDivision


@pytest.fixture
def calculator():
    return LineCalculatorDivision()


def test_calculate_two_same_numbers(calculator):
    assert calculator.calculate_line("") == 0
