import pytest

from . import InputTextParser
from ...internal import InstructionType, InstructionConditionType


@pytest.fixture
def input_text_parser():
    return InputTextParser()


def test_register_name(input_text_parser):
    parsed_input = input_text_parser.parse("reg inc 5 if cond > 1")
    assert "reg" == parsed_input.instructions[0]._register_name


def test_instruction_type_inc(input_text_parser):
    parsed_input = input_text_parser.parse("reg inc 5 if cond > 1")
    assert InstructionType.INC == parsed_input.instructions[0]._instruction_type


def test_instruction_type_dec(input_text_parser):
    parsed_input = input_text_parser.parse("reg dec 5 if cond > 1")
    assert InstructionType.DEC == parsed_input.instructions[0]._instruction_type


def test_value_to_apply(input_text_parser):
    parsed_input = input_text_parser.parse("reg inc 10001 if cond > 1")
    assert 10001 == parsed_input.instructions[0]._value_to_apply


def test_condition_register(input_text_parser):
    parsed_input = input_text_parser.parse("reg inc 5 if cond > 1")
    assert "cond" == parsed_input.instructions[0]._condition_register


def test_condition_type_greater(input_text_parser):
    parsed_input = input_text_parser.parse("reg inc 5 if cond > 1")
    assert InstructionConditionType.GREATER == parsed_input.instructions[0]._condition_type


def test_condition_type_greater_equals(input_text_parser):
    parsed_input = input_text_parser.parse("reg inc 5 if cond >= 1")
    assert InstructionConditionType.GREATER_EQUALS == parsed_input.instructions[0]._condition_type


def test_condition_type_lesser(input_text_parser):
    parsed_input = input_text_parser.parse("reg inc 5 if cond < 1")
    assert InstructionConditionType.LESSER == parsed_input.instructions[0]._condition_type


def test_condition_type_lesser_equals(input_text_parser):
    parsed_input = input_text_parser.parse("reg inc 5 if cond <= 1")
    assert InstructionConditionType.LESSER_EQUALS == parsed_input.instructions[0]._condition_type


def test_condition_type_equals(input_text_parser):
    parsed_input = input_text_parser.parse("reg inc 5 if cond == 1")
    assert InstructionConditionType.EQUALS == parsed_input.instructions[0]._condition_type


def test_condition_type_not_equals(input_text_parser):
    parsed_input = input_text_parser.parse("reg inc 5 if cond != 1")
    assert InstructionConditionType.NOT_EQUALS == parsed_input.instructions[0]._condition_type


def test_condition_value(input_text_parser):
    parsed_input = input_text_parser.parse("reg inc 5 if cond != 98765")
    assert 98765 == parsed_input.instructions[0]._condition_value


def test_multiple_lines(input_text_parser):
    parsed_input = input_text_parser.parse("reg inc 5 if cond > 1\n" * 3)
    assert 3 == len(parsed_input.instructions)
