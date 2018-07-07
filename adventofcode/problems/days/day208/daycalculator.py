from adventofcode.problems.framework import AbstractDayCalculator

if __name__ == "__main__":
    from adventofcode.problems.days.day208.solver import Solver
    from adventofcode.problems.days.day208.internal import InputTextParser
else:
    from .solver import Solver
    from .internal import InputTextParser


class DayCalculator(AbstractDayCalculator):
    def _get_main_calculator_file_path(self):
        return __file__

    def _create_new_solver(self):
        return Solver()

    def _get_input_file_parser(self):
        return InputTextParser()


if __name__ == "__main__":
    DayCalculator().calculate_both_parts_and_print_results()
