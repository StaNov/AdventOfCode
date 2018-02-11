from adventofcode.problems.utils import AbstractSolver
from .internal import TrampolineMaze


class Solver(AbstractSolver):
    def _solve_1_internal(self, input_):
        return solve(input_, False)

    def _solve_2_internal(self, input_):
        return solve(input_, True)


def solve(input_, use_decrementing_maze):
    maze = TrampolineMaze(input_, use_decrementing_maze)
    maze.process_until_finished()
    return maze.get_steps_done()
