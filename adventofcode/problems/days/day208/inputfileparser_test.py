from .inputfileparser import InputFileParser
from .parsedinput import Instruction


def test_register_name_1():
    parsed_input = InputFileParser().parse("b inc 5 if a > 1")
    assert "b" == parsed_input.instructions[0].register_name


def test_register_name_2():
    parsed_input = InputFileParser().parse("cde inc 5 if a > 1")
    assert "cde" == parsed_input.instructions[0].register_name


def test_instruction_type_inc():
    parsed_input = InputFileParser().parse("b inc 5 if a > 1")
    assert Instruction.Type.INC == parsed_input.instructions[0].type


def test_instruction_type_dec():
    parsed_input = InputFileParser().parse("b dec 5 if a > 1")
    assert Instruction.Type.DEC == parsed_input.instructions[0].type


def test_value_to_apply_1():
    parsed_input = InputFileParser().parse("b inc 5 if a > 1")
    assert 5 == parsed_input.instructions[0].value_to_apply


def test_value_to_apply_2():
    parsed_input = InputFileParser().parse("b inc 10001 if a > 1")
    assert 10001 == parsed_input.instructions[0].value_to_apply


def test_condition_register():
    parsed_input = InputFileParser().parse("b inc 5 if a > 1")
    assert "a" == parsed_input.instructions[0].condition_register
