from .direction import Direction


class Position:

    def __init__(self):
        super().__init__()
        self._position_x = 0
        self._position_y = 0

    def get_coordinates(self):
        return self._position_x, self._position_y

    def move(self, direction):
        self._position_x, self._position_y = self.get_coordinates_in_direction(direction)

    def get_coordinates_in_direction(self, direction):
        if direction == Direction.RIGHT:
            return self._position_x + 1, self._position_y

        if direction == Direction.UP:
            return self._position_x, self._position_y + 1

        if direction == Direction.LEFT:
            return self._position_x - 1, self._position_y

        if direction == Direction.DOWN:
            return self._position_x, self._position_y - 1
