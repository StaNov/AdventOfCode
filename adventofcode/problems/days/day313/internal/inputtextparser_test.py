from .direction import Direction
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

    cars = parsed.cars
    assert len(cars) == 1

    car = cars[0]
    assert car.position == (2, 1)
    assert car.direction is Direction.UP


def test_more_cars():
    parsed = InputTextParser().parse(
        " ^  ^\n"
        "^ ^  "
    )

    parsed_positions = map(lambda car: car.position, parsed.cars)

    assert set(parsed_positions) == {(1, 0), (4, 0), (0, 1), (2, 1)}


def test_direction_down():
    parsed = InputTextParser().parse("v")
    assert parsed.cars[0].direction is Direction.DOWN


def test_direction_right():
    parsed = InputTextParser().parse(">")
    assert parsed.cars[0].direction is Direction.RIGHT


def test_direction_left():
    parsed = InputTextParser().parse("<")
    assert parsed.cars[0].direction is Direction.LEFT
