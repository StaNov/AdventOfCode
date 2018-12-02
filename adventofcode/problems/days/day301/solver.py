from adventofcode.problems.framework import AbstractSolver
from .internal import HelperClass


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.helper = HelperClass()

    def _solve_1_internal(self, input_):
        if len(input_) == 0:
            return 0

        result = 0

        for number in input_:
            digits_part = number[1:]
            result += int(digits_part)

        return result

    def _solve_2_internal(self, input_):
        # TODO
        return self.helper.helper_method(input_)
