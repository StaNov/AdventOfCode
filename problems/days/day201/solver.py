from problems.utils import AbstractSolver
from .internal import CaptchaComputer


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.helper = CaptchaComputer()

    def solve_1_internal(self, input_string):
        return CaptchaComputer().compute_captcha(input_string, 1)

    def solve_2_internal(self, input_string):
        return CaptchaComputer().compute_captcha(input_string, len(input_string) // 2)
