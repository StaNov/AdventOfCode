from adventofcode.problems.framework import AbstractSolver
from .internal import SameLettersCounter


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()

    def _solve_1_internal(self, input_):

        doubles_count = 0
        triples_count = 0

        for line in input_:
            if SameLettersCounter(line).has_n_same_letters(2):
                doubles_count += 1

            if SameLettersCounter(line).has_n_same_letters(3):
                triples_count += 1

        return doubles_count * triples_count

    def _solve_2_internal(self, input_):
        # TODO
        # return self.helper.has_two_same_letters(input_)
        return 0
