from adventofcode.problems.utils import AbstractDayCalculator
if __name__ == "__main__":
    from adventofcode.problems.days.day02.solver import Solver
else:
    from .solver import Solver


class DayCalculator(AbstractDayCalculator):
    def _get_main_calculator_file_path(self):
        return __file__

    def _create_new_solver(self):
        return Solver()


if __name__ == "__main__":
    DayCalculator().calculate_both_parts_and_print_results()
