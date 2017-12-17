from .internal import SpiralIncremental, SpiralSumming, SpiralComputing
from problems.utils import AbstractSolver


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()

    def solve_1_internal(self, input_string):
        spiral_length = int(input_string)
        spiral = SpiralComputing(spiral_length)

        return spiral.distance_from_start()

    def solve_1_internal_incremental_version(self, input_string):
        spiral_length = int(input_string)
        spiral = SpiralIncremental()

        spiral.generate_numbers(spiral_length - 1)

        return spiral.get_last_number_distance()

    def solve_2_internal(self, input_string):
        limit = int(input_string)
        spiral = SpiralSumming()

        while spiral.get_last_number() <= limit:
            spiral.generate_number()

        return spiral.get_last_number()
