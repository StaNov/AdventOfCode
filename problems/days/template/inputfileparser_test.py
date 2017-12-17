from .inputfileparser import InputFileParser


def test_parse():
    # TODO
    assert ["abc", "def", "ghi"] == InputFileParser().parse("abc\ndef\nghi")
