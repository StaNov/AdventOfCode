from enum import Enum

from .direction import Direction


class RoadType(Enum):
    STRAIGHT = 0
    LEFT_TO_UP = 1

    def rotate(self, initial_direction):
        if self is RoadType.STRAIGHT:
            return initial_direction

        if initial_direction is Direction.LEFT:
            return Direction.DOWN

        if initial_direction is Direction.DOWN:
            return Direction.LEFT

        if initial_direction is Direction.RIGHT:
            return Direction.UP

        return Direction.RIGHT
