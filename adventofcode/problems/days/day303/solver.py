from adventofcode.problems.framework import AbstractSolver
from .internal import SantaSuit


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.santa_suit = SantaSuit()

    def _solve_1_internal(self, input_):
        self.apply_patches(input_)
        return self.santa_suit.get_overlapping_count()

    def _solve_2_internal(self, input_):
        # TODO
        # return self.santa_suit.helper_method(input_)
        return 0

    def apply_patches(self, input_):
        for patch in input_:
            self.santa_suit.saw_patch(patch)
