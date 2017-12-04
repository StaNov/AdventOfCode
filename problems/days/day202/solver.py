from problems.utils import AbstractSolver
from .internal import LineCalculatorMinMax, LineCalculatorDivision


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()

    def solve_1_internal(self, input_string):
        return _solve(input_string, LineCalculatorMinMax())

    def solve_2_internal(self, input_string):
        return _solve(input_string, LineCalculatorDivision())


def _solve(input_string, line_calculator):
    result = 0

    for line in input_string.splitlines():
        result += line_calculator.calculate_line(line)

    return result
