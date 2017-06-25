from utils import AbstractSolver
from .internal import LettersProcessor


class Solver(AbstractSolver):
    def __init__(self):
        self.letters_processor = LettersProcessor()

    def solve_1_internal(self, input_string):
        for char in input_string:
            self.letters_processor.process_letter(char)

        return self.letters_processor.get_processed_output_length()

    def solve_2_internal(self, input_string):
        # TODO
        return self.letters_processor.helper_method(input_string)
