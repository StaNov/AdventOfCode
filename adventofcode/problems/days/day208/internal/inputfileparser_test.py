from .inputfileparser import InputFileParser
from .instruction import InstructionType, InstructionConditionType


def test_register_name_1():
    parsed_input = InputFileParser().parse("b inc 5 if a > 1")
    assert "b" == parsed_input.instructions[0].register_name


def test_register_name_2():
    parsed_input = InputFileParser().parse("cde inc 5 if a > 1")
    assert "cde" == parsed_input.instructions[0].register_name


def test_instruction_type_inc():
    parsed_input = InputFileParser().parse("b inc 5 if a > 1")
    assert InstructionType.INC == parsed_input.instructions[0]._instruction_type


def test_instruction_type_dec():
    parsed_input = InputFileParser().parse("b dec 5 if a > 1")
    assert InstructionType.DEC == parsed_input.instructions[0]._instruction_type


def test_value_to_apply_1():
    parsed_input = InputFileParser().parse("b inc 5 if a > 1")
    assert 5 == parsed_input.instructions[0]._value_to_apply


def test_value_to_apply_2():
    parsed_input = InputFileParser().parse("b inc 10001 if a > 1")
    assert 10001 == parsed_input.instructions[0]._value_to_apply


def test_condition_register_1():
    parsed_input = InputFileParser().parse("b inc 5 if a > 1")
    assert "a" == parsed_input.instructions[0].condition_register


def test_condition_register_2():
    parsed_input = InputFileParser().parse("b inc 5 if abcde > 1")
    assert "abcde" == parsed_input.instructions[0].condition_register


def test_condition_type_greater():
    parsed_input = InputFileParser().parse("b inc 5 if a > 1")
    assert InstructionConditionType.GREATER == parsed_input.instructions[0].condition_type


def test_condition_type_greater_equals():
    parsed_input = InputFileParser().parse("b inc 5 if a >= 1")
    assert InstructionConditionType.GREATER_EQUALS == parsed_input.instructions[0].condition_type


def test_condition_type_lesser():
    parsed_input = InputFileParser().parse("b inc 5 if a < 1")
    assert InstructionConditionType.LESSER == parsed_input.instructions[0].condition_type


def test_condition_type_lesser_equals():
    parsed_input = InputFileParser().parse("b inc 5 if a <= 1")
    assert InstructionConditionType.LESSER_EQUALS == parsed_input.instructions[0].condition_type


def test_condition_type_equals():
    parsed_input = InputFileParser().parse("b inc 5 if a == 1")
    assert InstructionConditionType.EQUALS == parsed_input.instructions[0].condition_type


def test_condition_type_not_equals():
    parsed_input = InputFileParser().parse("b inc 5 if a != 1")
    assert InstructionConditionType.NOT_EQUALS == parsed_input.instructions[0].condition_type


def test_condition_value_1():
    parsed_input = InputFileParser().parse("b inc 5 if a != 1")
    assert 1 == parsed_input.instructions[0].condition_value


def test_condition_value_2():
    parsed_input = InputFileParser().parse("b inc 5 if a != 98765")
    assert 98765 == parsed_input.instructions[0].condition_value


def test_multiple_lines():
    parsed_input = InputFileParser().parse("b inc 5 if a > 1\nb inc 5 if a > 1\nb inc 5 if a > 1")
    assert 3 == len(parsed_input.instructions)
