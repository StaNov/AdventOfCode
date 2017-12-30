from . import LineParser


def test_parse():
    assert LineParser.parse("aaaaa-bbb-z-y-x-123[abxyz]") == ("aaaaa-bbb-z-y-x", 123, "abxyz")
