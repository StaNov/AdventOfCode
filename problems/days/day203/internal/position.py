class Position:

    def __init__(self):
        super().__init__()
        self._position_x = 0
        self._position_y = 0

    def get_coordinates(self):
        return self._position_x, self._position_y

    def move(self, direction):
        self._position_x += 1
