from .inputtextparser import InputTextParser


def test_parse():
    assert ["abc", "def", "ghi"] == InputTextParser().parse("abc\ndef\nghi")
