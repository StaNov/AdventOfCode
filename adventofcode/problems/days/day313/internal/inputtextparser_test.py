from .inputtextparser import InputTextParser


def test_empty_input():
    parsed = InputTextParser().parse("")
    assert len(parsed.cars) == 0


def test_one_car_facing_up():
    parsed = InputTextParser().parse("^")

    assert len(parsed.cars) == 1
    assert parsed.cars[0].position == (0, 0)
