from adventofcode.problems.framework.inputfileparser import InputFileParser


def test_parse_empty_string():
    assert "" == InputFileParser().parse("")


def test_parse():
    assert "abc" == InputFileParser().parse("abc")
