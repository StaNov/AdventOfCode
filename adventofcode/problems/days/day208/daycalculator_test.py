import pytest

from .daycalculator import DayCalculator


@pytest.fixture
def day_calculator():
    return DayCalculator()


def test_main_1_on_empty_input():
    assert 0 == DayCalculator("").calculate_part_1()


def test_main_1_with_all_conditions_true():
    custom_input = (
        "a inc 10 if a == 0\n"
        "a inc 10 if b <= 0\n"
        "a inc 10 if c > -1\n"
        "a inc 10 if d < 2\n"
        "a dec -10 if e >= 0")

    assert 50 == DayCalculator(custom_input).calculate_part_1()


def test_main_1(day_calculator):
    # TODO
    # assert 0 == day_calculator.calculate_part_1()
    pass


def test_main_2(day_calculator):
    # TODO
    # assert 0 == day_calculator.calculate_part_2()
    pass
