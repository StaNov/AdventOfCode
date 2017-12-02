from problems.utils import AbstractSolver
from .internal import HelperClass


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.helper = HelperClass()

    def solve_1_internal(self, input_string):
        for i in range(len(input_string) - 1):
            if input_string[i] == input_string[i + 1]:
                return int(input_string[i])

        return 0

    def solve_2_internal(self, input_string):
        # TODO
        return self.helper.helper_method(input_string)
