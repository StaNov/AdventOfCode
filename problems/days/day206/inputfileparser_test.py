from .inputfileparser import InputFileParser


def test_parse_empty_string():
    assert [] == InputFileParser().parse("")


def test_parse_one_number():
    assert [1] == InputFileParser().parse("1")


def test_parse_one_different_number():
    assert [2] == InputFileParser().parse("2")


def test_parse_two_numbers():
    assert [1, 2] == InputFileParser().parse("1\t2")
