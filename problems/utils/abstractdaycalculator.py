from . import inputfilereader
from .inputfileparser import InputFileParser


class AbstractDayCalculator:
    def __init__(self):
        file_content = self._load_file_content()
        self._input = self.get_input_file_parser().parse(file_content)

    def calculate_both_parts_and_print_results(self):
        result_1 = self.calculate_part_1()

        _print_separator()
        print("FIRST RESULT IS:\n\n" + str(result_1))

        print()

        _print_separator()
        result_2 = self.calculate_part_2()
        print("SECOND RESULT IS:\n\n" + str(result_2))

    def calculate_part_1(self):
        solver = self.create_new_solver()
        return solver.solve_1(self._input)

    def calculate_part_2(self):
        solver = self.create_new_solver()
        return solver.solve_2(self._input)

    def create_new_solver(self):
        raise Exception("Abstract method not implemented!")

    def get_main_calculator_file_path(self):
        raise Exception("Abstract method not implemented!")

    def get_input_file_parser(self):
        return InputFileParser()

    def _load_file_content(self):
        main_calculator_file_name = self.get_main_calculator_file_path()
        return inputfilereader.read_file_to_string(main_calculator_file_name)


def _print_separator():
    print("=" * 40)
