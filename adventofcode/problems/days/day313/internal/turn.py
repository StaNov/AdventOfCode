from enum import Enum


class Turn(Enum):
    NO_TURN = 0

    def of(self, direction):
        return direction
