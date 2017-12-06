class Spiral:
    def __init__(self, length):
        self._length = length
        self._last_number_in_loop = 0

        self._compute_last_number_in_loop()

    def distance_from_start(self):
        if self._length == 1:
            return 0

        return 1 + self._length % 2

    def get_last_number_in_loop(self):
        return self._last_number_in_loop

    def _compute_last_number_in_loop(self):
        i = 1
        while i**2 < self._length:
            i += 2

        self._last_number_in_loop = i ** 2
