from .inputtextparser import InputTextParser


def test_parse_empty_input():
    assert [] == InputTextParser().parse("")
