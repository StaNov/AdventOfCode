import pytest
from .main import MainCalculator


@pytest.fixture
def main():
    return MainCalculator()


def test_main_1(main):
    assert main.calculate_part_1() == 123


@pytest.mark.skip
def test_main_2(main):
    # TODO
    assert main.calculate_part_2() == 0
