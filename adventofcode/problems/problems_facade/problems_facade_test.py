import pytest

from . import problems_facade


def test_get_available_days():
    days = problems_facade.get_available_days()

    for i in range(1, 4):
        assert i in days

    assert -1 not in days


def test_available_days_are_returned_sorted():
    days = problems_facade.get_available_days()

    sorted_days = days.copy()
    sorted_days.sort()

    assert sorted_days == days


def test_get_day_calculator_existing():
    for i in range(1, 4):
        _day_calculator_is_instantiable(i)


def test_get_day_calculator_not_existing():
    with pytest.raises(problems_facade.DayNotExistsException):
        problems_facade.get_day_calculator(-1)


@pytest.mark.parametrize("parametrized_day_number", problems_facade.get_available_days())
def test_all_days_instantiable(parametrized_day_number):
    _day_calculator_is_instantiable(parametrized_day_number)


def _day_calculator_is_instantiable(day_number):
    calculator = problems_facade.get_day_calculator(day_number)
    assert hasattr(calculator, "calculate_part_1")
