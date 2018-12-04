import pytest

from .daycalculator import DayCalculator


@pytest.fixture
def calculator():
    return DayCalculator()


def test_main_1(calculator):
    # TODO
    assert 0 == calculator.calculate_part_1()


def test_main_2(calculator):
    # TODO
    assert 0 == calculator.calculate_part_2()
