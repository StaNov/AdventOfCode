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


@pytest.mark.skip
def test_main_1(calculator):
    # TODO
    assert 0 == calculator.calculate_part_1()


# TODO
@pytest.mark.skip
def test_example_2_1(calculator):
    # TODO
    assert 0 == DayCalculator("Part 2, example 1").calculate_part_2()


# TODO
@pytest.mark.skip
def test_example_2_2(calculator):
    # TODO
    assert 0 == DayCalculator("Part 2, example 2").calculate_part_2()


@pytest.mark.skip
def test_main_2(calculator):
    # TODO
    assert 0 == calculator.calculate_part_2()
