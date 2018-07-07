from . import inputfilereader
from .defaultinputtextparser import DefaultInputTextParser


class AbstractDayCalculator:
    def __init__(self, custom_input_text=None):
        self._input_text = custom_input_text if custom_input_text is not None else self._load_input_file_content()
        self._input_text_parser = self._get_input_file_parser()

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
        return DefaultInputTextParser()

    def _load_input_file_content(self):
        main_calculator_file_name = self._get_main_calculator_file_path()
        return inputfilereader.read_file_to_string(main_calculator_file_name)

    def _get_parsed_input(self):
        return self._input_text_parser.parse(self._input_text)


def _print_separator():
    print("=" * 40)
