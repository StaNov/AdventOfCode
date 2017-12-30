from .inputfileparser import InputFileParser


def test_parse():
    assert [1, 500, -98765] == InputFileParser().parse("1\n500\n-98765")
