from adventofcode.problems.framework import AbstractSolver
from .internal import HelperClass


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.helper = HelperClass()

    def _solve_1_internal(self, input_):
        if len(input_) < 2:
            return 0

        patch_1 = input_[0]
        patch_2 = input_[1]

        cloth = {}

        for i in range(patch_1.position_x, patch_1.position_x + patch_1.size_x):
            for j in range(patch_1.position_y, patch_1.position_y + patch_1.size_y):
                current = cloth.get((i, j), 0)
                cloth[(i, j)] = current + 1

        for i in range(patch_2.position_x, patch_2.position_x + patch_2.size_x):
            for j in range(patch_2.position_y, patch_2.position_y + patch_2.size_y):
                current = cloth.get((i, j), 0)
                cloth[(i, j)] = current + 1

        return len(list(filter(lambda x: x > 1, cloth.values())))

    def _solve_2_internal(self, input_):
        # TODO
        return self.helper.helper_method(input_)
