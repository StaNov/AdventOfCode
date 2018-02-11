import pytest

from . import RegisterCalculator
from .parsedinput import Instruction


@pytest.fixture
def calculator():
    return RegisterCalculator()


def test_zero_is_highest_value_after_calculator_is_created(calculator):
    assert 0 == calculator.highest_value


def test_apply_one_instruction_1(calculator):
    calculator.apply_instruction(
        Instruction("a", Instruction.Type.INC, 10, "a", Instruction.ConditionType.EQUALS, 0)
    )
    assert 10 == calculator.highest_value


def test_apply_one_instruction_2(calculator):
    calculator.apply_instruction(Instruction(
        "a", Instruction.Type.INC, 20, "a", Instruction.ConditionType.EQUALS, 0)
    )
    assert 20 == calculator.highest_value


def test_apply_two_instructions_first_bigger(calculator):
    calculator.apply_instruction(
        Instruction("a", Instruction.Type.INC, 20, "a", Instruction.ConditionType.EQUALS, 0)
    )
    calculator.apply_instruction(
        Instruction("b", Instruction.Type.INC, 10, "a", Instruction.ConditionType.EQUALS, 0)
    )
    assert 20 == calculator.highest_value


def test_apply_two_instructions_same_register(calculator):
    calculator.apply_instruction(
        Instruction("a", Instruction.Type.INC, 20, "a", Instruction.ConditionType.GREATER_EQUALS, 0)
    )
    calculator.apply_instruction(
        Instruction("a", Instruction.Type.INC, 10, "a", Instruction.ConditionType.GREATER_EQUALS, 0)
    )
    assert 30 == calculator.highest_value


def test_decrement_instruction(calculator):
    calculator.apply_instruction(
        Instruction("a", Instruction.Type.DEC, 10, "a", Instruction.ConditionType.NOT_EQUALS, 0)
    )
    assert -10 == calculator.highest_value


def test_false_condition_keeps_zero_value(calculator):
    calculator.apply_instruction(
        Instruction("a", Instruction.Type.INC, 20, "a", Instruction.ConditionType.LESSER, 0)
    )
    assert 0 == calculator.highest_value
