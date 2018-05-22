from .inputfileparser import InputFileParser
from .instruction import InstructionType, InstructionConditionType


def test_register_name():
    parsed_input = InputFileParser().parse("reg inc 5 if cond > 1")
    assert "reg" == parsed_input.instructions[0].register_name


def test_instruction_type_inc():
    parsed_input = InputFileParser().parse("reg inc 5 if cond > 1")
    assert InstructionType.INC == parsed_input.instructions[0]._instruction_type


def test_instruction_type_dec():
    parsed_input = InputFileParser().parse("reg dec 5 if cond > 1")
    assert InstructionType.DEC == parsed_input.instructions[0]._instruction_type


def test_value_to_apply():
    parsed_input = InputFileParser().parse("reg inc 10001 if cond > 1")
    assert 10001 == parsed_input.instructions[0]._value_to_apply


def test_condition_register():
    parsed_input = InputFileParser().parse("reg inc 5 if cond > 1")
    assert "cond" == parsed_input.instructions[0].condition_register


def test_condition_type_greater():
    parsed_input = InputFileParser().parse("reg inc 5 if cond > 1")
    assert InstructionConditionType.GREATER == parsed_input.instructions[0].condition_type


def test_condition_type_greater_equals():
    parsed_input = InputFileParser().parse("reg inc 5 if cond >= 1")
    assert InstructionConditionType.GREATER_EQUALS == parsed_input.instructions[0].condition_type


def test_condition_type_lesser():
    parsed_input = InputFileParser().parse("reg inc 5 if cond < 1")
    assert InstructionConditionType.LESSER == parsed_input.instructions[0].condition_type


def test_condition_type_lesser_equals():
    parsed_input = InputFileParser().parse("reg inc 5 if cond <= 1")
    assert InstructionConditionType.LESSER_EQUALS == parsed_input.instructions[0].condition_type


def test_condition_type_equals():
    parsed_input = InputFileParser().parse("reg inc 5 if cond == 1")
    assert InstructionConditionType.EQUALS == parsed_input.instructions[0].condition_type


def test_condition_type_not_equals():
    parsed_input = InputFileParser().parse("reg inc 5 if cond != 1")
    assert InstructionConditionType.NOT_EQUALS == parsed_input.instructions[0].condition_type


def test_condition_value():
    parsed_input = InputFileParser().parse("reg inc 5 if cond != 98765")
    assert 98765 == parsed_input.instructions[0].condition_value


def test_multiple_lines():
    parsed_input = InputFileParser().parse("reg inc 5 if cond > 1\n" * 3)
    assert 3 == len(parsed_input.instructions)
