from adventofcode.problems.framework import AbstractSolver
from .internal import HelperClass


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.helper = HelperClass()

    def _solve_1_internal(self, input_):
        if len(input_) < 2:
            return 0

        return input_[0].size_x * input_[0].size_y

    def _solve_2_internal(self, input_):
        # TODO
        return self.helper.helper_method(input_)
