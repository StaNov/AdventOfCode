from utils import AbstractSolver
from .internal import Interpreter


class Solver(AbstractSolver):
    def initialize_internal(self):
        self.interpreter = None

    def solve_1_internal(self, input_string):
        self._run_interpreter(input_string)
        return self.interpreter.get_lightens()

    def solve_2_internal(self, input_string):
        self._run_interpreter(input_string)
        result = self.interpreter.get_display()
        print(result)
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
