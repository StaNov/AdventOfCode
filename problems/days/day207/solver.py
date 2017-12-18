from problems.utils import AbstractSolver
from .internal import ProgramTree


class Solver(AbstractSolver):
    def solve_1_internal(self, input_):
        return ProgramTree(input_).get_root_program_name()

    def solve_2_internal(self, input_):
        # TODO
        return 0
