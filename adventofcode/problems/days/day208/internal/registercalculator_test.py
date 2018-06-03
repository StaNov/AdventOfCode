import pytest

from . import RegisterCalculator


@pytest.fixture
def calculator():
    return RegisterCalculator()


def test_zero_is_highest_value_after_calculator_is_created(calculator):
    assert 0 == calculator.highest_value


def test_apply_one_instruction(calculator):
    calculator.apply_instruction(
        InstructionMock("a", 10)
    )
    assert 10 == calculator.highest_value


def test_apply_two_instructions(calculator):
    calculator.apply_instruction(
        InstructionMock("a", 20)
    )
    calculator.apply_instruction(
        InstructionMock("b", 10)
    )
    assert 20 == calculator.highest_value


def test_apply_two_instructions_same_register(calculator):
    calculator.apply_instruction(
        InstructionMock("a", 20)
    )
    calculator.apply_instruction(
        InstructionMock("a", 10)
    )
    assert 30 == calculator.highest_value


# TODO move somewhere else
@pytest.mark.skip
def test_decrement_instruction(calculator):
    calculator.apply_instruction(
        Instruction("a", InstructionType.DEC, 10)
    )
    assert -10 == calculator.highest_value


# TODO move somewhere else
@pytest.mark.skip
def test_false_condition_keeps_zero_value(calculator):
    calculator.apply_instruction(
        InstructionWithCondition("a", InstructionType.INC, 20, "a", InstructionConditionType.LESSER, 0)
    )
    assert 0 == calculator.highest_value


class InstructionMock:

    def __init__(self, register_name, value_to_add):
        self._register_name = register_name
        self._value_to_add = value_to_add

    def apply_on_registers(self, registers):
        registers.add(self._register_name, self._value_to_add)
