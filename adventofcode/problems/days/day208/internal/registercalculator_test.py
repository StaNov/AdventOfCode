import pytest

from . import RegisterCalculator
from ..parsedinput import Instruction


@pytest.fixture
def calculator():
    return RegisterCalculator()


def test_zero_is_highest_value_after_calculator_is_created(calculator):
    assert 0 == calculator.highest_value


def test_apply_one_instruction(calculator):
    calculator.apply_instruction(Instruction("a", Instruction.Type.INC, 10, "a", Instruction.ConditionType.EQUALS, 0))
    assert 10 == calculator.highest_value
