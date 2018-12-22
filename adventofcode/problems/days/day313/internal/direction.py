from enum import Enum


class Direction(Enum):
    DOWN = 0
    UP = 1

    def apply_on(self, position):
        original_x, original_y = position

        if self is Direction.DOWN:
            return (
                original_x,
                original_y + 1
            )
