from utils import AbstractSolver
from .internal import Interpreter


class Solver(AbstractSolver):
    def initialize_internal(self):
        self.interpreter = None

    def solve_1_internal(self, input_string):
        lines = input_string.splitlines()

        self._init_interpreter(lines)

        for line in lines[2:]:
            self.interpreter.command(line)

        return self.interpreter.get_lightens()

    def _init_interpreter(self, lines):
        width = int(lines[0])
        height = int(lines[1])
        self.interpreter = Interpreter(width, height)

    def solve_2_internal(self, input_string):
        # TODO
        # return self.interpreter.helper_method(input_string)
        pass
