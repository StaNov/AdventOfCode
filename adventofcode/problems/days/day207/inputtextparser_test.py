from .inputtextparser import InputTextParser


def test_parse_empty():
    assert [] == InputTextParser().parse("")


def test_parse_one_line():
    assert [("abc", 123, [])] == InputTextParser().parse("abc (123)")


def test_parse_two_lines():
    assert [("abc", 123, []), ("defg", 45, [])] == InputTextParser().parse("abc (123)\ndefg (45)")


def test_parse_one_line_subprograms():
    assert [("abc", 123, ["sub1", "sub2", "sub3"])] == InputTextParser().parse("abc (123) -> sub1, sub2, sub3")
