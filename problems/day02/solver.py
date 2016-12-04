from .internal import Keyboard, KeyboardController


class Solver:
    @staticmethod
    def solve_1(input_string):
        lines = input_string.split("\n")
        result = ""
        keyboard = Keyboard(5)
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

        return int(result)

    @staticmethod
    def solve_2(input_string):
        return 0
