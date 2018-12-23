from .inputtextparser import InputTextParser


def test_empty_input():
    parsed = InputTextParser().parse("")
    assert len(parsed.cars) == 0
