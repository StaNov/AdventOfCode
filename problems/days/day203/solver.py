from problems.utils import AbstractSolver
from .internal import SpiralComputing


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()

    def solve_1_internal(self, input_string):
        spiral_length = int(input_string)
        spiral = SpiralComputing(spiral_length)
        return spiral.distance_from_start()

    def solve_2_internal(self, input_string):
        # TODO
        # return self.helper.helper_method(input_string)
        return 0
