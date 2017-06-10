import re

from utils import AbstractSolver
from .internal import HelperClass


class Solver(AbstractSolver):
    def initialize_internal(self):
        self.helper = HelperClass()

    def solve_1_internal(self, input_string):
        lines = input_string.splitlines()

        if len(lines) < 3:
            return 0

        match = re.fullmatch("rect (\w+)x(\w+)", lines[2])
        return int(match.group(1)) * int(match.group(2))

    def solve_2_internal(self, input_string):
        # TODO
        return self.helper.helper_method(input_string)
