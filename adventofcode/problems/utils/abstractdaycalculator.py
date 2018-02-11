from . import inputfilereader
from .inputfileparser import InputFileParser


class AbstractDayCalculator:
    def __init__(self):
        self._file_content = self._load_file_content()
        self._file_parser = self._get_input_file_parser()

    def calculate_both_parts_and_print_results(self):
        print("Calculating first result...")
        result_1 = self.calculate_part_1()

        _print_separator()
        print("FIRST RESULT IS:\n\n" + str(result_1))

        print()

        print("Calculating second result...")
        result_2 = self.calculate_part_2()
        _print_separator()
        print("SECOND RESULT IS:\n\n" + str(result_2))

    def calculate_part_1(self):
        solver = self._create_new_solver()
        input_ = self._get_parsed_input()
        return solver.solve_1(input_)

    def calculate_part_2(self):
        solver = self._create_new_solver()
        input_ = self._get_parsed_input()
        return solver.solve_2(input_)

    def _create_new_solver(self):
        raise NotImplementedError("Abstract method not implemented!")

    def _get_main_calculator_file_path(self):
        raise NotImplementedError("Abstract method not implemented!")

    def _get_input_file_parser(self):
        return InputFileParser()

    def _load_file_content(self):
        main_calculator_file_name = self._get_main_calculator_file_path()
        return inputfilereader.read_file_to_string(main_calculator_file_name)

    def _get_parsed_input(self):
        return self._file_parser.parse(self._file_content)


def _print_separator():
    print("=" * 40)
