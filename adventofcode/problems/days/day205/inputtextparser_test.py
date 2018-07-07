from .inputtextparser import InputTextParser


def test_parse():
    assert [1, 500, -98765] == InputTextParser().parse("1\n500\n-98765")
