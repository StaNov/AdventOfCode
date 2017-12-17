import pytest

from problems.utils import testsuite
from .main import DayCalculator


@pytest.fixture
def main():
    return DayCalculator()


def test_main_1(main):
    assert 375042 == main.calculate_part_1()


@testsuite.time_expensive
def test_main_2(main):
    assert 28707598 == main.calculate_part_2()
