class Keyboard:
    def __init__(self, key=5):
        self._current_key = key
        self.set_key(key)

    def get_key(self):
        return self._current_key

    def set_key(self, key):
        if key not in range(1, 10):
            raise ValueError("Value " + str(key) + " is not on the keyboard!")

        self._current_key = key
