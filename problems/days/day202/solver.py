from .internal.linessummer import LinesSummer
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
    return LinesSummer(line_calculator).sum_processed_lines(input_string)
