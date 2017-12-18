import pytest
from .main import DayCalculator


@pytest.fixture
def main():
    return DayCalculator()


def test_main_1(main):
    assert 11137 == main.calculate_part_1()


def test_main_2(main):
    assert 1037 == main.calculate_part_2()
