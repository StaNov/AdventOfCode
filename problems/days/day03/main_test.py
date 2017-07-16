import pytest
from .main import DayCalculator


@pytest.fixture
def main():
    return DayCalculator()


def test_main_1(main):
    assert main.calculate_part_1() == 983


def test_main_2(main):
    assert main.calculate_part_2() == 1836
