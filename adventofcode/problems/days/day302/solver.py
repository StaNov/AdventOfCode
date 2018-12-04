from adventofcode.problems.framework import AbstractSolver
from .internal import SameLettersCounter


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()

    def _solve_1_internal(self, input_):
        if len(input_) == 0:
            return 0

        line = input_[0]

        return (
            (1 if SameLettersCounter(line).has_n_same_letters(2) else 0)
            +
            (1 if SameLettersCounter(line).has_n_same_letters(3) else 0)
        )

    def _solve_2_internal(self, input_):
        # TODO
        return self.helper.has_two_same_letters(input_)
