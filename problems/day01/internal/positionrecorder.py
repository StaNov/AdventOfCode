class PositionRecorder:

    def __init__(self):
        self._positions = []
        self._already_found = False
        self._current_position = (0, 0)
        self._positions.append(self._current_position)

    def record(self, position):
        if self._already_found:
            raise Exception("Visited position was already found!")

        if (position[0] != self._current_position[0] and
                position[1] != self._current_position[1]):
            raise ValueError("New position is not in line with the previous one!")

        is_first_step = True
        for x in _inclusive_range(self._current_position[0], position[0]):
            for y in _inclusive_range(self._current_position[1], position[1]):
                if is_first_step:
                    is_first_step = False
                    continue

                if (x, y) in self._positions:
                    self._already_found = True
                    return x, y

                self._positions.append((x, y))

        self._current_position = position


def _inclusive_range(begin, end):
    if begin > end:
        return range(begin, end - 1, -1)

    return range(begin, end + 1, 1)
