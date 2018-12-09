import pytest

from .daycalculator import DayCalculator


@pytest.fixture
def calculator():
    return DayCalculator()


def test_example_1_empty_input(calculator):
    assert 0 == DayCalculator("").calculate_part_1()


# TODO
@pytest.mark.skip
def test_example_1_two_same_squares(calculator):
    assert 4 == DayCalculator(
        "#1 @ 1,1: 2x2\n"
        "#2 @ 1,1: 2x2\n").calculate_part_1()


# TODO
@pytest.mark.skip
def test_example_1_1(calculator):
    assert 4 == DayCalculator(
        "#1 @ 1,3: 4x4\n"
        "#2 @ 3,1: 4x4\n"
        "#3 @ 5,5: 2x2").calculate_part_1()


# TODO
@pytest.mark.skip
def test_example_1_2(calculator):
    assert 0 == DayCalculator("Part 2, example 2").calculate_part_1()


# TODO
@pytest.mark.skip
def test_main_1(calculator):
    assert 0 == calculator.calculate_part_1()


# TODO
@pytest.mark.skip
def test_example_2_1(calculator):
    assert 0 == DayCalculator("Part 2, example 1").calculate_part_2()


# TODO
@pytest.mark.skip
def test_example_2_2(calculator):
    assert 0 == DayCalculator("Part 2, example 2").calculate_part_2()


# TODO
@pytest.mark.skip
def test_main_2(calculator):
    assert 0 == calculator.calculate_part_2()
