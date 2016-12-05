from . import LineParser


def test_parse():
    assert LineParser.parse("123 456 789") == (123, 456, 789)
