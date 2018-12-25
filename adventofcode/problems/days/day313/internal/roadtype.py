from enum import Enum

from .direction import Direction


class RoadType(Enum):
    STRAIGHT = 0
    LEFT_TO_UP = 1
    RIGHT_TO_UP = 2

    def rotate(self, initial_direction):
        if self is RoadType.STRAIGHT:
            return initial_direction

        if self is RoadType.LEFT_TO_UP:
            if initial_direction is Direction.LEFT:
                return Direction.DOWN

            if initial_direction is Direction.DOWN:
                return Direction.LEFT

            if initial_direction is Direction.RIGHT:
                return Direction.UP

            return Direction.RIGHT

        if self is RoadType.RIGHT_TO_UP:
            if initial_direction is Direction.LEFT:
                return Direction.UP

            if initial_direction is Direction.DOWN:
                return Direction.RIGHT

            if initial_direction is Direction.RIGHT:
                return Direction.DOWN

            return Direction.LEFT
