from .position import Position
from .direction import Direction


class Spiral:

    def __init__(self):
        super().__init__()
        self._spiral = {}
        self._current_number = 1
        self._current_position = Position()
        self._current_direction = Direction.RIGHT

        self._spiral[(0, 0)] = 1

    def get_last_number(self):
        return self._current_number

    def generate_number(self):
        self._current_number += 1
        self._current_position.move(self._current_direction)
        self._put_current_number_to_current_position()
        self._change_direction_if_needed()

    def _put_current_number_to_current_position(self):
        self._spiral[self._current_position.get_coordinates()] = self._current_number

    def get_last_number_distance(self):
        return self._current_number - 1

    def _change_direction_if_needed(self):
        x, y = self._current_position.get_coordinates()

        if abs(y) + 1 == x and self._current_direction == Direction.RIGHT or\
                abs(x) == abs(y) and self._current_direction != Direction.RIGHT:
            self._current_direction = self._current_direction.rotate()
