import pytest

from . import LineCalculator


@pytest.fixture
def calculator():
    return LineCalculator()


def test_calculator_method(calculator):
    assert calculator.calculate_line("1") == 1


def test_with_exception():
    # TODO
    with pytest.raises(Exception):
        raise Exception("Test exception in test")
