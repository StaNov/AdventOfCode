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

        max_size = 0
        for line in lines[2:]:
            match = re.fullmatch("rect (\w+)x(\w+)", line)
            size = int(match.group(1)) * int(match.group(2))
            if size > max_size:
                max_size = size

        return max_size

    def solve_2_internal(self, input_string):
        # TODO
        return self.helper.helper_method(input_string)
