from adventofcode.problems.framework import AbstractSolver
from .internal import SameLettersCounter


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.helper = SameLettersCounter()

    def _solve_1_internal(self, input_):
        if len(input_) == 0:
            return 0

        line = input_[0]

        if "bb" in line:
            return 1

        return 2

    def _solve_2_internal(self, input_):
        # TODO
        return self.helper.helper_method(input_)
