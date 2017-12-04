import pytest

from . import LineCalculator


@pytest.fixture
def calculator():
    return LineCalculator()


def test_calculate_two_same_numbers(calculator):
    assert calculator.calculate_line("1 1") == 0


def test_calculate_two_different_numbers(calculator):
    assert calculator.calculate_line("5 2") == 3


def test_with_exception():
    # TODO
    with pytest.raises(Exception):
        raise Exception("Test exception in test")
