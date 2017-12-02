from problems.utils import AbstractSolver
from .internal import HelperClass


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.helper = HelperClass()

    def solve_1_internal(self, input_string):
        return solve(input_string, len(input_string) - 1, 1, True)

    def solve_2_internal(self, input_string):
        return 2 * solve(input_string, len(input_string) // 2, len(input_string) // 2, False)


def solve(input_string, range_upper_bound, second_digit_index_offset, include_circular):
    result = 0

    for i in range(range_upper_bound):
        digit_1 = input_string[i]
        digit_2 = input_string[i + second_digit_index_offset]

        if digit_1 == digit_2:
            result += int(digit_1)

    if include_circular and len(input_string) > 2 and input_string[0] == input_string[-1]:
        result += int(input_string[0])

    return result
