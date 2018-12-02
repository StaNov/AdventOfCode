from adventofcode.problems.framework import AbstractSolver
from .internal import HelperClass


def parse_input_value(value):
    sign = value[0]
    number = int(value[1:])

    if sign == "-":
        number = -number

    return number


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.helper = HelperClass()

    def _solve_1_internal(self, input_):
        result = 0

        for value in input_:
            result += parse_input_value(value)

        return result

    def _solve_2_internal(self, input_):
        # TODO
        return self.helper.helper_method(input_)
