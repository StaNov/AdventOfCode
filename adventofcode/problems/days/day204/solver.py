from adventofcode.problems.utils import AbstractSolver
from .internal import PasswordChecker, PasswordCheckerAnagramic, ValidPasswordsCounter


class Solver(AbstractSolver):
    def solve_1_internal(self, input_string):
        return _count_valid_passwords(PasswordChecker(), input_string)

    def solve_2_internal(self, input_string):
        return _count_valid_passwords(PasswordCheckerAnagramic(), input_string)


def _count_valid_passwords(checker, input_string):
    counter = ValidPasswordsCounter(checker)
    return counter.count(input_string)
