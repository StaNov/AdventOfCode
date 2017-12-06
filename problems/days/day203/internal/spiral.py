class Spiral:
    def __init__(self, length):
        self._length = length
        self._last_number_in_loop = None
        self._loop_number = None
        self._corner_numbers = None
        self._distance_from_corner = None

        self._compute_loop_numbers()
        self._compute_corner_numbers()
        self._compute_distance_from_corner()

    def distance_from_start(self):
        if self._length == 1:
            return 0

        return self._loop_number + self._length % 2

    def _compute_loop_numbers(self):
        i = 1
        while i**2 < self._length:
            i += 2

        self._last_number_in_loop = i ** 2
        self._loop_number = i//2

    def _compute_corner_numbers(self):
        self._corner_numbers = {
            self._last_number_in_loop,
            self._last_number_in_loop - 2 * self._loop_number,
            self._last_number_in_loop - 4 * self._loop_number,
            self._last_number_in_loop - 6 * self._loop_number
        }

    def _compute_distance_from_corner(self):
        if self._length == 1:
            self._distance_from_corner = 0
            return

        self._distance_from_corner = 1
