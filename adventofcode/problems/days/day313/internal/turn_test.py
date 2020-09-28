from adventofcode.problems.days.day313.internal.direction import Direction
from adventofcode.problems.days.day313.internal.turn import Turn


def test_no_turn_same_direction():
    assert Turn.NO_TURN.of(Direction.RIGHT) is Direction.RIGHT
    assert Turn.NO_TURN.of(Direction.LEFT) is Direction.LEFT
    assert Turn.NO_TURN.of(Direction.UP) is Direction.UP
    assert Turn.NO_TURN.of(Direction.DOWN) is Direction.DOWN
