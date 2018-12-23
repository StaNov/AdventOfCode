from .direction import Direction
from .inputtextparser import InputTextParser


def test_empty_input():
    parsed = InputTextParser().parse("")
    assert len(parsed.cars) == 0


def test_direction_up():
    _assert_direction("^", Direction.UP)


def test_direction_down():
    _assert_direction("v", Direction.DOWN)


def test_direction_right():
    _assert_direction(">", Direction.RIGHT)


def test_direction_left():
    _assert_direction("<", Direction.LEFT)


def _assert_direction(letter, expected_direction):
    parsed = InputTextParser().parse(letter)
    assert parsed.cars[0].direction is expected_direction


def test_one_car_position():
    parsed = InputTextParser().parse(
        "     \n"
        "  ^  "
    )

    cars = parsed.cars
    assert len(cars) == 1
    assert cars[0].position == (2, 1)


def test_more_cars_positions():
    parsed = InputTextParser().parse(
        " ^  ^\n"
        "^ ^  "
    )

    parsed_positions = map(lambda car: car.position, parsed.cars)

    assert set(parsed_positions) == {(1, 0), (4, 0), (0, 1), (2, 1)}
