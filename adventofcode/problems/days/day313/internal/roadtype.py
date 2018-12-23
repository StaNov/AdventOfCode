from enum import Enum

from .direction import Direction


class RoadType(Enum):
    STRAIGHT = 0
    LEFT_TO_UP = 1

    def rotate(self, initial_rotation):
        if self is RoadType.STRAIGHT:
            return initial_rotation

        return Direction.UP
