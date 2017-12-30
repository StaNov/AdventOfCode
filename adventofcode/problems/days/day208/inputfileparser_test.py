from .inputfileparser import InputFileParser


def test_register_name_1():
    parsed_input = InputFileParser().parse("b inc 5 if a > 1")
    assert "b" == parsed_input.instructions[0].register_name


def test_register_name_2():
    parsed_input = InputFileParser().parse("cde inc 5 if a > 1")
    assert "cde" == parsed_input.instructions[0].register_name
