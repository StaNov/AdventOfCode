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


    def get_last_number_distance(self):
        return self._current_number - 1
