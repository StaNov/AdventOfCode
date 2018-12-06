from .inputtextparser import InputTextParser


def test_parse():
    # TODO
    assert ["abc", "def", "ghi"] == InputTextParser().parse("abc\ndef\nghi")
