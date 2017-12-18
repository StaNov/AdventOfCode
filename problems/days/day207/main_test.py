import pytest
from .main import DayCalculator


@pytest.fixture
def main():
    return DayCalculator()


def test_main_1(main):
    # TODO
    # assert 0 == main.calculate_part_1()
    pass


def test_main_2(main):
    # TODO
    # assert 0 == main.calculate_part_2()
    pass
