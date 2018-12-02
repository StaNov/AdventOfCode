import pytest

from .daycalculator import DayCalculator


@pytest.fixture
def calculator():
    return DayCalculator()


def test_example_1_1():
    assert 3 == DayCalculator("+1\n-2\n+3\n+1").calculate_part_1()


def test_example_1_2():
    assert 3 == DayCalculator("+1\n+1\n+1").calculate_part_1()


def test_example_1_3():
    assert 0 == DayCalculator("+1\n+1\n-2").calculate_part_1()


def test_example_1_4():
    assert -6 == DayCalculator("-1\n-2\n-3").calculate_part_1()


def test_main_1(calculator):
    assert 516 == calculator.calculate_part_1()


def test_example_2_1():
    assert 0 == DayCalculator("+1\n-1").calculate_part_2()


def test_example_2_2():
    assert 10 == DayCalculator("+3\n+3\n+4\n-2\n-4").calculate_part_2()


def test_example_2_3():
    assert 5 == DayCalculator("-6\n+3\n+8\n+5\n-6").calculate_part_2()


def test_example_2_4():
    assert 14 == DayCalculator("+7\n+7\n-2\n-7\n-4").calculate_part_2()


def test_main_2(calculator):
    assert 71892 == calculator.calculate_part_2()
