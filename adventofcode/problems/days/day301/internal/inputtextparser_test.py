from .inputtextparser import InputTextParser


def test_parse_empty_input():
    assert [] == InputTextParser().parse("")


def test_parse_digits():
    assert [123, -567] == InputTextParser().parse("+123\n-567")
