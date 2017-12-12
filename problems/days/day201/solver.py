from problems.utils import AbstractSolver
from .internal import HelperClass


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.helper = HelperClass()

    def solve_1_internal(self, input_string):
        return solve(input_string, 1)

    def solve_2_internal(self, input_string):
        return solve(input_string, len(input_string) // 2)


def solve(input_string, second_digit_index_offset):
    if len(input_string) < 3:
        raise Exception("Input must be longer than 3 characters.")

    result = 0

    for i in range(len(input_string)):
        digit_1 = input_string[i]
        digit_2 = input_string[(i + second_digit_index_offset) % len(input_string)]

        if digit_1 == digit_2:
            result += int(digit_1)

    return result
