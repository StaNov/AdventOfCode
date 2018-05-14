from adventofcode.problems.framework import AbstractSolver
from .internal import RegisterCalculator


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.helper = RegisterCalculator()

    def _solve_1_internal(self, input_):
        # TODO
        # return self.helper.helper_method(input_)
        return 0

    def _solve_2_internal(self, input_):
        # TODO
        # return self.helper.helper_method(input_)
        return 0
