from utils import AbstractSolver
from .internal import HelperClass


class Solver(AbstractSolver):
    def initialize_internal(self):
        self.helper = HelperClass()

    def solve_1_internal(self, input_string):
        return len(input_string)
        # TODO
        # return self.helper.helper_method(input_string)

    def solve_2_internal(self, input_string):
        # TODO
        return self.helper.helper_method(input_string)
