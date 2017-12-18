from .inputfileparser import InputFileParser


def test_parse_empty():
    assert {} == InputFileParser().parse("")


def test_parse_one_line():
    assert {"abc": 123} == InputFileParser().parse("abc (123)")
