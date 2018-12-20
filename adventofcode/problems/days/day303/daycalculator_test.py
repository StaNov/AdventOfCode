import pytest

from adventofcode.problems.framework import testsuite
from .daycalculator import DayCalculator


@pytest.fixture
def calculator():
    return DayCalculator()


def test_example_1_empty_input(calculator):
    assert 0 == DayCalculator("").calculate_part_1()


def test_example_1_two_same_squares(calculator):
    assert 4 == DayCalculator(
        "#1 @ 1,1: 2x2\n"
        "#2 @ 1,1: 2x2\n").calculate_part_1()


def test_example_1_1(calculator):
    assert 4 == DayCalculator(
        "#1 @ 1,3: 4x4\n"
        "#2 @ 3,1: 4x4\n"
        "#3 @ 5,5: 2x2").calculate_part_1()


@testsuite.time_expensive
def test_main_1(calculator):
    assert 111266 == calculator.calculate_part_1()


def test_example_2_one_patch_always_intact(calculator):
    assert 1 == DayCalculator("#1 @ 1,1: 2x2").calculate_part_2()


def test_example_2_full_example(calculator):
    assert 3 == DayCalculator(
        "#1 @ 1,3: 4x4\n"
        "#2 @ 3,1: 4x4\n"
        "#3 @ 5,5: 2x2").calculate_part_2()


@testsuite.time_expensive
def test_main_2(calculator):
    assert 266 == calculator.calculate_part_2()
