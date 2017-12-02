from problems.utils import AbstractSolver
from .internal import HelperClass


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.helper = HelperClass()

    def solve_1_internal(self, input_string):
        if len(input_string) < 2:
            return 0

        if len(input_string) == 2:
            if input_string[0] == input_string[1]:
                return int(input_string[0])

            return 0

        if input_string[0] != input_string[1] and input_string[1] != input_string[2]:
            return 0

        return int(input_string[1])

    def solve_2_internal(self, input_string):
        # TODO
        return self.helper.helper_method(input_string)
