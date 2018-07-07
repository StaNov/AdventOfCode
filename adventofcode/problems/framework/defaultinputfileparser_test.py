from adventofcode.problems.framework.defaultinputtextparser import DefaultInputTextParser


def test_parse_empty_string():
    assert "" == DefaultInputTextParser().parse("")


def test_parse():
    assert "abc" == DefaultInputTextParser().parse("abc")
