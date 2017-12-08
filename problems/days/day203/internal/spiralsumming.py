from .spiralincremental import SpiralIncremental


class SpiralSumming(SpiralIncremental):

    def _get_next_number_to_generate(self):
        result = 0
        current_x, current_y = self._current_position.get_coordinates()

        for x in range(current_x - 1, current_x + 2):
            for y in range(current_y - 1, current_y + 2):
                result += self._get_value_at_position((x, y))

        return result
