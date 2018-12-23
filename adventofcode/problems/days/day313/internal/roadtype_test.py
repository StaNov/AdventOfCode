from .direction import Direction
from .roadtype import RoadType


def test_straight_does_not_change_direction():
    initial_rotation = object()

    final_rotation = RoadType.STRAIGHT.rotate(initial_rotation)

    assert final_rotation is initial_rotation


def test_left_to_up_turns_left_to_up():
    initial_rotation = Direction.LEFT
    final_rotation = RoadType.LEFT_TO_UP.rotate(initial_rotation)

    assert final_rotation is Direction.UP


def test_left_to_up_turns_down_to_right():
    initial_rotation = Direction.DOWN
    final_rotation = RoadType.LEFT_TO_UP.rotate(initial_rotation)

    assert final_rotation is Direction.RIGHT
