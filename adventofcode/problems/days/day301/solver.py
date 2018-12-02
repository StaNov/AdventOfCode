from adventofcode.problems.framework import AbstractSolver


class Solver(AbstractSolver):
    def _solve_1_internal(self, input_):
        return sum(input_)

    def _solve_2_internal(self, input_):
        visited_frequencies = {0}
        current_sum = 0

        while True:
            for number in input_:
                current_sum += number

                if current_sum in visited_frequencies:
                    return current_sum

                visited_frequencies.add(current_sum)
