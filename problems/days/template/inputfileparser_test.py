from .inputfileparser import InputFileParser


def test_parse():
    assert ["abc", "def", "ghi"] == InputFileParser().parse("abc\ndef\nghi")
