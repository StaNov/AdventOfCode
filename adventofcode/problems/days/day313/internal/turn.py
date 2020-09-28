from enum import Enum

from adventofcode.problems.days.day313.internal.direction import Direction


class Turn(Enum):
    NO_TURN = 0
    LEFT = 1
    RIGHT = 2

    def of(self, direction):
        if self is Turn.NO_TURN:
            return direction

        if self is Turn.LEFT:
            return Direction((direction.value + 1) % len(Direction))

        if self is Turn.RIGHT:
            return Direction((direction.value - 1) % len(Direction))
