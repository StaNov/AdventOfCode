from .inputfileparser import InputFileParser


def test_parse_empty():
    assert {} == InputFileParser().parse("")


def test_parse_one_line():
    assert {"abc": (123, [])} == InputFileParser().parse("abc (123)")


def test_parse_two_lines():
    assert {"abc": (123, []), "defg": (45, [])} == InputFileParser().parse("abc (123)\ndefg (45)")


def test_parse_one_line_subprograms():
    assert {"abc": (123, ["sub1", "sub2", "sub3"])} == InputFileParser().parse("abc (123) -> sub1, sub2, sub3")
