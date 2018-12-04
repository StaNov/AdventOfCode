import pytest

from .daycalculator import DayCalculator


@pytest.fixture
def calculator():
    return DayCalculator()


def test_example_1_0(calculator):
    assert 0 == DayCalculator("").calculate_part_1()


# TODO
@pytest.mark.skip
def test_example_1_1(calculator):
    assert 0 == DayCalculator("abcdef").calculate_part_1()


# TODO
@pytest.mark.skip
def test_example_1_2(calculator):
    assert 2 == DayCalculator("bababc").calculate_part_1()


def test_example_1_3(calculator):
    assert 1 == DayCalculator("abbcde").calculate_part_1()


# TODO
@pytest.mark.skip
def test_example_1_4(calculator):
    assert 1 == DayCalculator("abcccd").calculate_part_1()


# TODO
@pytest.mark.skip
def test_example_1_5(calculator):
    assert 1 == DayCalculator("aabcdd").calculate_part_1()


# TODO
@pytest.mark.skip
def test_example_1_6(calculator):
    assert 1 == DayCalculator("abcdee").calculate_part_1()


# TODO
@pytest.mark.skip
def test_example_1_7(calculator):
    assert 1 == DayCalculator("ababab").calculate_part_1()


# TODO
@pytest.mark.skip
def test_example_1_8(calculator):
    assert 12 == DayCalculator(
        "abcdef"
        "bababc"
        "abbcde"
        "abcccd"
        "aabcdd"
        "abcdee"
        "ababab").calculate_part_1()


@pytest.mark.skip
def test_main_1(calculator):
    # TODO
    assert 0 == calculator.calculate_part_1()


def test_example_2_1(calculator):
    # TODO
    assert 0 == DayCalculator("Part 2, example 1").calculate_part_2()


def test_example_2_2(calculator):
    # TODO
    assert 0 == DayCalculator("Part 2, example 2").calculate_part_2()


@pytest.mark.skip
def test_main_2(calculator):
    # TODO
    assert 0 == calculator.calculate_part_2()
