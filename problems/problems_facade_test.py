import pytest
from problems import problems_facade


@pytest.mark.skip
def test_get_available_days():
    days = problems_facade.get_available_days()

    for i in range(0, 4):
        assert i in days

    assert -1 not in days


def test_get_day_calculator_existing():
    for i in range(1, 4):
        day_calculator = problems_facade.get_day_calculator(i)
        day_calculator.calculate_part_1()


def test_get_day_calculator_not_existing():
    with pytest.raises(problems_facade.DayNotExistsException):
        problems_facade.get_day_calculator(-1)
