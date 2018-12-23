from enum import Enum


class RoadType(Enum):
    STRAIGHT = 0

    def rotate(self, initial_rotation):
        return initial_rotation
