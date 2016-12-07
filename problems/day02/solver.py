from .internal import Keyboard, KeyboardAdvanced, KeyboardController


class Solver:
    @staticmethod
    def solve_1(input_string):
        return Solver._solve(input_string, Keyboard())

    @staticmethod
    def solve_2(input_string):
        return Solver._solve(input_string, KeyboardAdvanced())

    @staticmethod
    def _solve(input_string, keyboard):
        lines = input_string.splitlines()
        result = ""
        ctrl = KeyboardController(keyboard)

        for line in lines:
            for char in line:
                if char == "L":
                    ctrl.move_left()
                    continue
                if char == "R":
                    ctrl.move_right()
                    continue
                if char == "U":
                    ctrl.move_up()
                    continue
                if char == "D":
                    ctrl.move_down()
                    continue

            result += str(keyboard.get_key())

        return result
