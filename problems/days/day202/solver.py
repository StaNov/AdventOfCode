from problems.utils import AbstractSolver
from .internal import HelperClass


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.helper = HelperClass()

    def solve_1_internal(self, input_string):
        lines = input_string.splitlines()

        if len(lines) == 0:
            return 0

        if len(lines) == 1:
            return int(lines[0])

        if len(lines) == 2:
            line1, line2 = lines
            return int(line1) + int(line2)

        return 0
        # return self.helper.helper_method(input_string)

    def solve_2_internal(self, input_string):
        # TODO
        return self.helper.helper_method(input_string)
