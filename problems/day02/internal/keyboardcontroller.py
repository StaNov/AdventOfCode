class KeyboardController:
    def __init__(self, keyboard):
        self._keyboard = keyboard

    def move_up(self):
        new_index = self._index()[0] - 1, self._index()[1]
        self._keyboard.set_index(new_index)

    def move_down(self):
        new_index = self._index()[0] + 1, self._index()[1]
        self._keyboard.set_index(new_index)

    def move_left(self):
        new_index = self._index()[0], self._index()[1] - 1
        self._keyboard.set_index(new_index)

    def move_right(self):
        new_index = self._index()[0], self._index()[1] + 1
        self._keyboard.set_index(new_index)

    def _index(self):
        return self._keyboard.get_index()
