class Spiral:
    def __init__(self, length):
        self._length = length
        self._last_number_in_loop = 0
        self._loop_number = 0

        self._compute_loop_numbers()

    def distance_from_start(self):
        if self._length == 1:
            return 0

        return 1 + self._length % 2

    def get_last_number_in_loop(self):
        return self._last_number_in_loop

    def _compute_loop_numbers(self):
        i = 1
        while i**2 < self._length:
            i += 2

        self._last_number_in_loop = i ** 2
        self._loop_number = i//2

    def get_loop_number(self):
        return self._loop_number
