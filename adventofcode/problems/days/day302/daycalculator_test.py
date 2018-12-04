import pytest

from .daycalculator import DayCalculator


@pytest.fixture
def calculator():
    return DayCalculator()


def test_example_1_1(calculator):
    # TODO
    assert 0 == DayCalculator("Part 1, example 1").calculate_part_1()


def test_example_1_2(calculator):
    # TODO
    assert 0 == DayCalculator("Part 2, example 2").calculate_part_1()


def test_main_1(calculator):
    # TODO
    assert 0 == calculator.calculate_part_1()


def test_example_2_1(calculator):
    # TODO
    assert 0 == DayCalculator("Part 2, example 1").calculate_part_2()


def test_example_2_2(calculator):
    # TODO
    assert 0 == DayCalculator("Part 2, example 2").calculate_part_2()


def test_main_2(calculator):
    # TODO
    assert 0 == calculator.calculate_part_2()
