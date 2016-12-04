class Keyboard:
    _values = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    _default_starting_index = 1, 1
    _unset_index = -1, -1

    def __init__(self, index=_default_starting_index):
        self._current_index = self._unset_index
        self.set_index(index)

    def get_key(self):
        return self._values[self._current_index[0]][self._current_index[1]]

    def get_index(self):
        return self._current_index

    def set_index(self, index):
        if (index[0] in range(0, len(self._values)) and
                index[1] in range(0, len(self._values[index[0]])) and
                self._values[index[0]][index[1]] is not None):
            self._current_index = index
            return

        if self._current_index == self._unset_index:
            raise ValueError("Index " + str(index) + " is not on the keyboard!")


class KeyboardAdvanced(Keyboard):
    _values = [
        [None, None, "1", None, None],
        [None, "2" , "3", "4" , None],
        ["5" , "6" , "7", "8" , "9" ],
        [None, "A" , "B", "C" , None],
        [None, None, "D", None, None]
    ]
    _default_starting_index = 2, 0

    def __init__(self, index=_default_starting_index):
        super().__init__(index)
