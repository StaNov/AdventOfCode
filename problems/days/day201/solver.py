from problems.utils import AbstractSolver
from .internal import HelperClass


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.helper = HelperClass()

    def solve_1_internal(self, input_string):
        result = 0

        for i in range(len(input_string) - 1):
            if input_string[i] == input_string[i + 1]:
                result += int(input_string[i])

        if len(input_string) > 2 and input_string[0] == input_string[-1]:
            result += int(input_string[0])

        return result

    def solve_2_internal(self, input_string):
        # TODO
        return self.helper.helper_method(input_string)
