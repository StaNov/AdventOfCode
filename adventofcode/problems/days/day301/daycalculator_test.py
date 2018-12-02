import pytest

from .daycalculator import DayCalculator


@pytest.fixture
def calculator():
    return DayCalculator()


def test_empty_input_gives_zero_result():
    assert 0 == DayCalculator("").calculate_part_1()


def test_example_1():
    assert 3 == DayCalculator("+1\n-2\n+3\n+1").calculate_part_1()


def test_example_2():
    assert 3 == DayCalculator("+1\n+1\n+1").calculate_part_1()


def test_example_3():
    assert 0 == DayCalculator("+1\n+1\n-2").calculate_part_1()


def test_example_4():
    assert -6 == DayCalculator("-1\n-2\n-3").calculate_part_1()


# TODO
@pytest.mark.skip
def test_main_1(calculator):
    # TODO
    assert 0 == calculator.calculate_part_1()


# TODO
@pytest.mark.skip
def test_main_2(calculator):
    # TODO
    assert 0 == calculator.calculate_part_2()
