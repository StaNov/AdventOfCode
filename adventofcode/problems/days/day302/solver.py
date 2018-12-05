from adventofcode.problems.framework import AbstractSolver
from .internal import SameLettersCounter, WordsWithoutOneLetterGenerator


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()

    def _solve_1_internal(self, input_):
        doubles_count = 0
        triples_count = 0

        for line in input_:
            if SameLettersCounter(line).has_n_same_letters(2):
                doubles_count += 1

            if SameLettersCounter(line).has_n_same_letters(3):
                triples_count += 1

        return doubles_count * triples_count

    def _solve_2_internal(self, input_):
        potential_solutions = set()

        for line in input_:
            for word_without_letter in WordsWithoutOneLetterGenerator(line).generate():
                if word_without_letter in potential_solutions:
                    return word_without_letter

                potential_solutions.add(word_without_letter)
