from adventofcode.problems.days.day313.internal.roadtype import RoadType


def test_straight_does_not_change_rotation():
    initial_rotation = object()

    final_rotation = RoadType.STRAIGHT.rotate(initial_rotation)

    assert final_rotation is initial_rotation
