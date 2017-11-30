from problems.utils import AbstractSolver
from .internal import *


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.letters_processor = None

    def solve_1_internal(self, input_string):
        self.letters_processor = LettersProcessor()
        return self.solve(input_string)

    def solve_2_internal(self, input_string):
        self.letters_processor = LettersProcessorRecursive()
        return self.solve(input_string)

    def solve(self, input_string):
        for char in input_string:
            self.letters_processor.process_letter(char)

        return self.letters_processor.get_processed_output_length()
