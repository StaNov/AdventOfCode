from problems.utils import AbstractSolver
from .internal import PasswordChecker, PasswordCheckerAnagramic, ValidPasswordsCounter


class Solver(AbstractSolver):
    def solve_1_internal(self, input_string):
        counter = ValidPasswordsCounter(PasswordChecker())
        return counter.count(input_string)

    def solve_2_internal(self, input_string):
        counter = ValidPasswordsCounter(PasswordCheckerAnagramic())
        return counter.count(input_string)
