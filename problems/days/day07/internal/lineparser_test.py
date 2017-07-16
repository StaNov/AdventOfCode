from . import LineParser


def test_parse():
    assert LineParser.parse("abcd[12345]efghi[6789]jkl") == (["abcd", "efghi", "jkl"], ["12345", "6789"])
