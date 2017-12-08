class Spiral:

    def __init__(self):
        super().__init__()
        self._last_number = 1

    def get_last_number(self) -> int:
        return self._last_number

    def generate_number(self):
        self._last_number += 1

    def get_last_number_distance(self):
        return self._last_number - 1
