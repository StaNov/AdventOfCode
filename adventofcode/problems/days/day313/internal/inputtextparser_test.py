from .inputtextparser import InputTextParser


def test_empty_input():
    parsed = InputTextParser().parse("")
    assert len(parsed.cars) == 0


def test_one_car_facing_up():
    parsed = InputTextParser().parse("^")

    assert len(parsed.cars) == 1
    assert parsed.cars[0].position == (0, 0)


def test_one_car_facing_up_another_position():
    parsed = InputTextParser().parse(
        "     \n"
        "  ^  "
    )

    assert len(parsed.cars) == 1
    assert parsed.cars[0].position == (2, 1)


def test_more_cars():
    parsed = InputTextParser().parse(
        " ^  ^\n"
        "^ ^  "
    )

    parsed_positions = map(lambda car: car.position, parsed.cars)

    assert set(parsed_positions) == {(1, 0), (4, 0), (0, 1), (2, 1)}
