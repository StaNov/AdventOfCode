import pytest

from .daycalculator import DayCalculator


@pytest.fixture
def calculator():
    return DayCalculator()


def test_example_1_1(calculator):
    assert 12 == DayCalculator(
        "abcdef\n"
        "bababc\n"
        "abbcde\n"
        "abcccd\n"
        "aabcdd\n"
        "abcdee\n"
        "ababab").calculate_part_1()


def test_main_1(calculator):
    assert 5000 == calculator.calculate_part_1()


def test_example_2_1(calculator):
    assert "fgij" == DayCalculator(
        "abcde\n"
        "fghij\n"
        "klmno\n"
        "pqrst\n"
        "fguij\n"
        "axcye\n"
        "wvxyz"
    ).calculate_part_2()


def test_main_2(calculator):
    assert "ymdrchgpvwfloluktajxijsqb" == calculator.calculate_part_2()
