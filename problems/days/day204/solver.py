from problems.utils import AbstractSolver
from .internal import PasswordChecker


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.checker = PasswordChecker()

    def solve_1_internal(self, input_string):
        valid_passwords_count = 0

        for line in input_string.splitlines():
            if self.checker.check(line):
                valid_passwords_count += 1

        return valid_passwords_count

    def solve_2_internal(self, input_string):
        # TODO
        # return self.helper.helper_method(input_string)
        return 0
