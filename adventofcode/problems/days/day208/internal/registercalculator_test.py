import pytest

from . import RegisterCalculator
from .instruction import InstructionType, Instruction


@pytest.fixture
def calculator():
    return RegisterCalculator()


def test_zero_is_highest_value_after_calculator_is_created(calculator):
    assert 0 == calculator.highest_value


def test_apply_one_instruction_1(calculator):
    calculator.apply_instruction(
        Instruction("a", InstructionType.INC, 10)
    )
    assert 10 == calculator.highest_value


def test_apply_one_instruction_2(calculator):
    calculator.apply_instruction(
        Instruction("a", InstructionType.INC, 20)
    )
    assert 20 == calculator.highest_value


def test_apply_two_instructions_first_bigger(calculator):
    calculator.apply_instruction(
        Instruction("a", InstructionType.INC, 20)
    )
    calculator.apply_instruction(
        Instruction("b", InstructionType.INC, 10)
    )
    assert 20 == calculator.highest_value


def test_apply_two_instructions_same_register(calculator):
    calculator.apply_instruction(
        Instruction("a", InstructionType.INC, 20)
    )
    calculator.apply_instruction(
        Instruction("a", InstructionType.INC, 10)
    )
    assert 30 == calculator.highest_value


def test_decrement_instruction(calculator):
    calculator.apply_instruction(
        Instruction("a", InstructionType.DEC, 10)
    )
    assert -10 == calculator.highest_value


# TODO what about this one?
@pytest.mark.skip
def test_false_condition_keeps_zero_value(calculator):
    calculator.apply_instruction(
        InstructionWithCondition("a", InstructionType.INC, 20, "a", InstructionConditionType.LESSER, 0)
    )
    assert 0 == calculator.highest_value
