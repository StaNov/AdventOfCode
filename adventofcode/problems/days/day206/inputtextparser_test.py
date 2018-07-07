from .inputtextparser import InputTextParser


def test_parse_empty_string():
    assert [] == InputTextParser().parse("")


def test_parse_one_number():
    assert [1] == InputTextParser().parse("1")


def test_parse_one_different_number():
    assert [2] == InputTextParser().parse("2")


def test_parse_two_numbers():
    assert [1, 2] == InputTextParser().parse("1\t2")
