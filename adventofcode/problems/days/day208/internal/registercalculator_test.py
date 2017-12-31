import pytest

from . import RegisterCalculator


@pytest.fixture
def calculator():
    return RegisterCalculator()


def test_zero_is_highest_value_after_calculator_is_created(calculator):
    assert 0 == calculator.highest_value
