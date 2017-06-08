from utils import AbstractSolver
from .internal import Keyboard, KeyboardAdvanced, KeyboardController


class Solver(AbstractSolver):
    def initialize_internal(self):
        self.keyboard = Keyboard()
        self.keyboard_advanced = KeyboardAdvanced()

    def solve_1_internal(self, input_string):
        self.controller = KeyboardController(self.keyboard)
        return self._solve(input_string)

    def solve_2_internal(self, input_string):
        self.controller = KeyboardController(self.keyboard_advanced)
        return self._solve(input_string)

    def _solve(self, input_string):
        lines = input_string.splitlines()
        result = ""

        for line in lines:
            for char in line:
                if char == "L":
                    self.controller.move_left()
                    continue
                if char == "R":
                    self.controller.move_right()
                    continue
                if char == "U":
                    self.controller.move_up()
                    continue
                if char == "D":
                    self.controller.move_down()
                    continue

            result += str(self.controller.get_key())

        return result
