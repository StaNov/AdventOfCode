# TODO redo the condition-independent tests only to Instruction

import pytest

from . import RegisterCalculator
from .instruction import InstructionType, InstructionConditionType, InstructionWithCondition


@pytest.fixture
def calculator():
    return RegisterCalculator()


def test_zero_is_highest_value_after_calculator_is_created(calculator):
    assert 0 == calculator.highest_value


def test_apply_one_instruction_1(calculator):
    calculator.apply_instruction(
        InstructionWithCondition("a", InstructionType.INC, 10, "a", InstructionConditionType.EQUALS, 0)
    )
    assert 10 == calculator.highest_value


def test_apply_one_instruction_2(calculator):
    calculator.apply_instruction(InstructionWithCondition(
        "a", InstructionType.INC, 20, "a", InstructionConditionType.EQUALS, 0)
    )
    assert 20 == calculator.highest_value


def test_apply_two_instructions_first_bigger(calculator):
    calculator.apply_instruction(
        InstructionWithCondition("a", InstructionType.INC, 20, "a", InstructionConditionType.EQUALS, 0)
    )
    calculator.apply_instruction(
        InstructionWithCondition("b", InstructionType.INC, 10, "a", InstructionConditionType.EQUALS, 0)
    )
    assert 20 == calculator.highest_value


def test_apply_two_instructions_same_register(calculator):
    calculator.apply_instruction(
        InstructionWithCondition("a", InstructionType.INC, 20, "a", InstructionConditionType.GREATER_EQUALS, 0)
    )
    calculator.apply_instruction(
        InstructionWithCondition("a", InstructionType.INC, 10, "a", InstructionConditionType.GREATER_EQUALS, 0)
    )
    assert 30 == calculator.highest_value


def test_decrement_instruction(calculator):
    calculator.apply_instruction(
        InstructionWithCondition("a", InstructionType.DEC, 10, "a", InstructionConditionType.NOT_EQUALS, 0)
    )
    assert -10 == calculator.highest_value


def test_false_condition_keeps_zero_value(calculator):
    calculator.apply_instruction(
        InstructionWithCondition("a", InstructionType.INC, 20, "a", InstructionConditionType.LESSER, 0)
    )
    assert 0 == calculator.highest_value
