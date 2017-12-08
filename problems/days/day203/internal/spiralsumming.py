from .spiralincremental import SpiralIncremental


class SpiralSumming(SpiralIncremental):

    def _get_next_number_to_generate(self):
        return 1
