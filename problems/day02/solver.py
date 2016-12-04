from .internal import Keyboard, KeyboardController


class Solver:
    @staticmethod
    def solve_1(input_string):
        lines = input_string.split("\n")

        for line in lines:
            keyboard = Keyboard(5)
            controller = KeyboardController(keyboard)
            # TODO

        return 0

    @staticmethod
    def solve_2(input_string):
        return 0
