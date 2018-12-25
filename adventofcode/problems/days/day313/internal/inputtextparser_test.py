from .roadtype import RoadType
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


def test_corner_left_to_up():
    parsed = InputTextParser().parse(
        "/"
    )

    assert RoadType.LEFT_TO_UP == parsed.roads[(0, 0)]
    assert None is parsed.roads.get((0, 1))


def test_corner_right_to_up():
    parsed = InputTextParser().parse(
        "\\"
    )

    assert RoadType.RIGHT_TO_UP == parsed.roads[(0, 0)]
    assert None is parsed.roads.get((0, 1))


def test_more_corners():
    parsed = InputTextParser().parse(
        r" /  " "\n"
        r"/ \ " "\n"
    )

    assert RoadType.LEFT_TO_UP == parsed.roads[(1, 0)]
    assert RoadType.LEFT_TO_UP == parsed.roads[(0, 1)]
    assert RoadType.RIGHT_TO_UP == parsed.roads[(2, 1)]
    assert None is parsed.roads.get((1, 1))
