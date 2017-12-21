from problems.utils import AbstractSolver
from .internal import ProgramTreeCreator


class Solver(AbstractSolver):
    def solve_1_internal(self, input_):
        return ProgramTreeCreator(input_).root_program.name

    def solve_2_internal(self, input_):
        # TODO
        return 0
