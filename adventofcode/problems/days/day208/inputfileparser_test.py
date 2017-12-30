from .inputfileparser import InputFileParser


def test_register_name():
    parsed_input = InputFileParser().parse("b inc 5 if a > 1")
    assert "b" == parsed_input.instructions[0].register_name
