from .direction import Direction


class Position:

    def __init__(self):
        super().__init__()
        self._position_x = 0
        self._position_y = 0

    def get_coordinates(self):
        return self._position_x, self._position_y

    def move(self, direction):
        if direction == Direction.RIGHT:
            self._position_x += 1

        if direction == Direction.UP:
            self._position_y += 1
