from utils import AbstractSolver
from .internal import Interpreter


class Solver(AbstractSolver):
    def initialize_internal(self):
        self.interpreter = Interpreter()

    def solve_1_internal(self, input_string):
        lines = input_string.splitlines()

        if len(lines) < 3:
            return 0

        self.interpreter = Interpreter()

        for line in lines[2:]:
            self.interpreter.command(line)

        return self.interpreter.get_lightens()

    def solve_2_internal(self, input_string):
        # TODO
        # return self.interpreter.helper_method(input_string)
        pass
