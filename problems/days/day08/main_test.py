import pytest
from .main import DayCalculator


@pytest.fixture
def main():
    return DayCalculator()


def test_main_1(main):
    assert main.calculate_part_1() == 123


def test_main_2(main):
    assert main.calculate_part_2() == \
            " XX  XXXX XXX  X  X XXX  XXXX XXX    XX XXX   XXX \n"\
            "X  X X    X  X X  X X  X    X X  X    X X  X X    \n"\
            "X  X XXX  XXX  X  X X  X   X  XXX     X X  X X    \n"\
            "XXXX X    X  X X  X XXX   X   X  X    X XXX   XX  \n"\
            "X  X X    X  X X  X X    X    X  X X  X X       X \n"\
            "X  X X    XXX   XX  X    XXXX XXX   XX  X    XXX  \n"
