from . import Keyboard


class KeyboardController:
    def __init__(self, keyboard):
        self._keyboard = keyboard

    def move_up(self):
        new_key = self._key() - 3
        if new_key >= 1:
            self._keyboard.set_key(new_key)

    def move_down(self):
        new_key = self._key() + 3
        if new_key <= 9:
            self._keyboard.set_key(new_key)

    def move_left(self):
        new_key = self._key() - 1
        if new_key % 3 != 0:
            self._keyboard.set_key(new_key)

    def move_right(self):
        new_key = self._key() + 1
        if new_key % 3 != 1:
            self._keyboard.set_key(new_key)

    def _key(self):
        return self._keyboard.get_key()
