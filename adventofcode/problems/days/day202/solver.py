from adventofcode.problems.framework import AbstractSolver
from .internal import LinesSummer, LineCalculatorMinMax, LineCalculatorDivision


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()

    def _solve_1_internal(self, input_):
        return _solve(input_, LineCalculatorMinMax)

    def _solve_2_internal(self, input_):
        return _solve(input_, LineCalculatorDivision)


def _solve(input_string, line_calculator_type):
    return LinesSummer(line_calculator_type).sum_processed_lines(input_string)
