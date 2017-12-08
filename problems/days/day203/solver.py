from .internal.spiral import Spiral
from problems.utils import AbstractSolver
from .internal import SpiralComputing


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()

    def solve_1_internal(self, input_string):
        spiral_length = int(input_string)
        spiral = Spiral()

        while spiral.get_last_number() < spiral_length:
            spiral.generate_number()

        return spiral.get_last_number_distance()

    def solve_2_internal(self, input_string):
        # TODO
        # return self.helper.helper_method(input_string)
        return 0
