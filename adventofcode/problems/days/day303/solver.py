from adventofcode.problems.framework import AbstractSolver
from .internal import SantaSuit


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.santa_suit = SantaSuit()

    def _solve_1_internal(self, input_):
        if len(input_) < 2:
            return 0

        patch_1 = input_[0]
        patch_2 = input_[1]

        self.santa_suit.saw_patch(patch_1)
        self.santa_suit.saw_patch(patch_2)

        return self.santa_suit.get_overlapping_count()

    def _solve_2_internal(self, input_):
        # TODO
        return self.santa_suit.helper_method(input_)
