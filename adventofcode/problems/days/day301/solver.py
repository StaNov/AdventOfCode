from adventofcode.problems.framework import AbstractSolver
from .internal import HelperClass


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.helper = HelperClass()

    def _solve_1_internal(self, input_):
        result = 0

        for value in input_:
            sign = value[0]
            number = int(value[1:])

            if sign == "-":
                number = -number

            result += number

        return result

    def _solve_2_internal(self, input_):
        # TODO
        return self.helper.helper_method(input_)
