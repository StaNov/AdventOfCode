from problems.utils import AbstractSolver
from .internal import ProgramTree


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.helper = ProgramTree({"test": (123, [])})

    def solve_1_internal(self, input_):
        # TODO
        return 0

    def solve_2_internal(self, input_):
        # TODO
        return 0
