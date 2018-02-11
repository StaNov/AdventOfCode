from adventofcode.problems.utils import AbstractSolver
from .internal import Interpreter


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.interpreter = None

    def _solve_1_internal(self, input_):
        self._run_interpreter(input_)
        return self.interpreter.get_lightens()

    def _solve_2_internal(self, input_):
        self._run_interpreter(input_)
        result = self.interpreter.get_display()
        return result

    def _run_interpreter(self, input_string):
        lines = input_string.splitlines()
        self._init_interpreter(lines)
        for line in lines[2:]:
            self.interpreter.command(line)

    def _init_interpreter(self, lines):
        width = int(lines[0])
        height = int(lines[1])
        self.interpreter = Interpreter(width, height)
