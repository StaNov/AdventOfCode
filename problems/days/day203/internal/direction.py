from enum import Enum


class Direction(Enum):
    DOWN = 0
    RIGHT = 1
    UP = 2
    LEFT = 3

    def rotate(self):
        return Direction((self.value + 1) % len(Direction))
