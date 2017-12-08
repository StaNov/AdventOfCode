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

    def generate_numbers(self, count):
        for __ in range(count):
            self.generate_number()

    def generate_number(self):
        self._current_number = self._get_next_number_to_generate()
        self._current_position.move(self._current_direction)
        self._put_current_number_to_current_position()
        self._turn_left_if_possible()

    def _put_current_number_to_current_position(self):
        self._spiral[self._current_position.get_coordinates()] = self._current_number

    def get_last_number_distance(self):
        x, y = self._current_position.get_coordinates()
        return abs(x) + abs(y)

    def _turn_left_if_possible(self):
        left_hand_direction = self._current_direction.rotate_left()
        left_hand_position = self._current_position.get_coordinates_in_direction(left_hand_direction)

        if self._get_value_at_position(left_hand_position) == 0:
            self._current_direction = left_hand_direction

    def _get_next_number_to_generate(self):
        return self._current_number + 1

    def _get_value_at_position(self, position):
        return self._spiral.get(position, 0)
