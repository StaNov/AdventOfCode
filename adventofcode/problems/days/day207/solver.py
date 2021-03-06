from adventofcode.problems.framework import AbstractSolver
from .internal import ProgramTreeCreator, UnbalanceFinder


class Solver(AbstractSolver):
    def _solve_1_internal(self, input_):
        return ProgramTreeCreator(input_).root_program.name

    def _solve_2_internal(self, input_):
        root_program = ProgramTreeCreator(input_).root_program
        return UnbalanceFinder(root_program).get_correct_weight_of_unbalanced_program()
