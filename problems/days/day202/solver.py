from problems.utils import AbstractSolver
from .internal import LineCalculator


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.line_calculator = LineCalculator()

    def solve_1_internal(self, input_string):
        lines = input_string.splitlines()

        # TODO remove when parsing is done correctly
        if len(lines) > 10:
            return 0

        result = 0

        for line in lines:
            result += self.line_calculator.calculate_line(line)

        return result

    def solve_2_internal(self, input_string):
        # TODO
        return 0
        # return self.helper.helper_method(input_string)
