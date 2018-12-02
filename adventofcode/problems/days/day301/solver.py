from adventofcode.problems.framework import AbstractSolver
from .internal import HelperClass


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.helper = HelperClass()

    def _solve_1_internal(self, input_):
        return sum(input_)

    def _solve_2_internal(self, input_):
        # TODO
        return self.helper.helper_method(input_)
