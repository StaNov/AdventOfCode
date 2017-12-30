from adventofcode.problems.utils import AbstractDayCalculator

if __name__ == "__main__":
    from adventofcode.problems.days.day208.solver import Solver
    from adventofcode.problems.days.day208.inputfileparser import InputFileParser
else:
    from .solver import Solver
    from .inputfileparser import InputFileParser


class DayCalculator(AbstractDayCalculator):
    def get_main_calculator_file_path(self):
        return __file__

    def create_new_solver(self):
        return Solver()

    def get_input_file_parser(self):
        return InputFileParser()


if __name__ == "__main__":
    DayCalculator().calculate_both_parts_and_print_results()
