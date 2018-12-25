from .direction import Direction
from .roadtype import RoadType


def test_straight_does_not_change_direction():
    mock_rotation = object()
    _assert_direction_changed_after_rotation_both_ways(RoadType.STRAIGHT, mock_rotation, mock_rotation)


def test_left_to_up_turns_left_to_down():
    _assert_direction_changed_after_rotation_both_ways(RoadType.LEFT_TO_UP, Direction.LEFT, Direction.DOWN)


def test_left_to_up_turns_right_to_up():
    _assert_direction_changed_after_rotation_both_ways(RoadType.LEFT_TO_UP, Direction.RIGHT, Direction.UP)


def test_right_to_up_turns_left_to_up():
    _assert_direction_changed_after_rotation_both_ways(RoadType.RIGHT_TO_UP, Direction.LEFT, Direction.UP)


def test_right_to_up_turns_right_to_down():
    _assert_direction_changed_after_rotation_both_ways(RoadType.RIGHT_TO_UP, Direction.RIGHT, Direction.DOWN)


def _assert_direction_changed_after_rotation_both_ways(road_type, direction_1, direction_2):
    assert direction_2 is road_type.rotate(direction_1)
    assert direction_1 is road_type.rotate(direction_2)
