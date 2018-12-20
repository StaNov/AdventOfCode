from adventofcode.problems.framework import AbstractSolver
from .internal import OreMine


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.helper = OreMine([])

    def _solve_1_internal(self, input_):
        # TODO
        return "3,3"

    def _solve_2_internal(self, input_):
        # TODO
        return 0
