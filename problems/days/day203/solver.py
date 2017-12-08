from .internal import SpiralIncremental
from problems.utils import AbstractSolver


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()

    def solve_1_internal(self, input_string):
        spiral_length = int(input_string)
        spiral = SpiralIncremental()

        spiral.generate_numbers(spiral_length - 1)

        return spiral.get_last_number_distance()

    def solve_2_internal(self, input_string):
        # TODO
        # return self.helper.helper_method(input_string)
        return 0
