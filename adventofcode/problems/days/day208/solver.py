from adventofcode.problems.framework import AbstractSolver
from .internal import RegisterCalculator


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.calculator = RegisterCalculator()

    def _solve_1_internal(self, input_):
        for instruction in input_.instructions:
            self.calculator.apply_instruction(instruction)

        return self.calculator.highest_value

    def _solve_2_internal(self, input_):
        # TODO
        # return self.helper.helper_method(input_)
        return 0
