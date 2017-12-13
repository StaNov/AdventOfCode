from problems.utils import AbstractSolver
from .internal import TrampolineMaze


class Solver(AbstractSolver):
    def solve_1_internal(self, input_):
        maze = TrampolineMaze(input_)
        maze.process_until_finished()
        return maze.get_steps_done()

    def solve_2_internal(self, input_):
        # TODO
        return 0
