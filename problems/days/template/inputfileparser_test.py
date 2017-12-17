from .inputfileparser import InputFileParser


def test_parse_empty_string():
    assert [] == InputFileParser().parse("")


def test_parse_one_number():
    assert [1] == InputFileParser().parse("1")
