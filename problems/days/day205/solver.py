from problems.utils import AbstractSolver
from .internal import TrampolineMaze, TrampolineMazeDecrementing


class Solver(AbstractSolver):
    def solve_1_internal(self, input_):
        return solve(TrampolineMaze(input_))

    def solve_2_internal(self, input_):
        return solve(TrampolineMazeDecrementing(input_))


def solve(maze):
    maze.process_until_finished()
    return maze.get_steps_done()
