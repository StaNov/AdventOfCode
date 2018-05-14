from adventofcode.problems.framework import AbstractSolver
from .internal import PasswordChecker, PasswordCheckerAnagramic, ValidPasswordsCounter


class Solver(AbstractSolver):
    def _solve_1_internal(self, input_):
        return _count_valid_passwords(PasswordChecker(), input_)

    def _solve_2_internal(self, input_):
        return _count_valid_passwords(PasswordCheckerAnagramic(), input_)


def _count_valid_passwords(checker, input_string):
    counter = ValidPasswordsCounter(checker)
    return counter.count(input_string)
