from adventofcode.problems.utils import AbstractSolver
from .internal import CaptchaComputer, CaptchaComputerHalfSlice


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.helper = CaptchaComputer()

    def _solve_1_internal(self, input_):
        return CaptchaComputer().compute_captcha(input_)

    def _solve_2_internal(self, input_):
        return CaptchaComputerHalfSlice().compute_captcha(input_)
