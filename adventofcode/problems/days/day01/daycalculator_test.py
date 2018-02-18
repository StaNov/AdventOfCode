import pytest

from .daycalculator import DayCalculator


@pytest.fixture
def main():
    return DayCalculator()


def test_main_1(main):
    assert main.calculate_part_1() == 262


def test_main_2(main):
    assert main.calculate_part_2() == 131
