from adventofcode.problems.framework import AbstractSolver
from .internal import SpiralIncremental, SpiralSumming, SpiralComputing


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()

    def _solve_1_internal(self, input_):
        spiral_length = int(input_)
        spiral = SpiralComputing(spiral_length)

        return spiral.distance_from_start()

    def solve_1_internal_incremental_version(self, input_string):
        spiral_length = int(input_string)
        spiral = SpiralIncremental()

        spiral.generate_numbers(spiral_length - 1)

        return spiral.get_last_number_distance()

    def _solve_2_internal(self, input_):
        limit = int(input_)
        spiral = SpiralSumming()

        while spiral.get_last_number() <= limit:
            spiral.generate_number()

        return spiral.get_last_number()
