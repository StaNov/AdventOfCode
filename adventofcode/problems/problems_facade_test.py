import pytest

from adventofcode.problems import problems_facade


def test_get_available_days():
    days = problems_facade.get_available_days()

    for i in range(1, 4):
        assert i in days

    assert -1 not in days


def test_get_day_calculator_existing():
    for i in range(1, 4):
        _test_instantiating_of_calculator_by_day_number(i)


def test_get_day_calculator_not_existing():
    with pytest.raises(problems_facade.DayNotExistsException):
        problems_facade.get_day_calculator(-1)


def test_all_days_instantiable():
    for i in problems_facade.get_available_days():
        _test_instantiating_of_calculator_by_day_number(i)


def _test_instantiating_of_calculator_by_day_number(day_number):
    calculator = problems_facade.get_day_calculator(day_number)
    assert hasattr(calculator, "calculate_part_1")
