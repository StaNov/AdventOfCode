from problems.utils import InputReader


class AbstractDayCalculator:
    def __init__(self):
        self._input_string = self._load_file_content()

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
        return solver.solve_1(self._input_string)

    def calculate_part_2(self):
        solver = self.create_new_solver()
        return solver.solve_2(self._input_string)

    def create_new_solver(self):
        raise Exception("Abstract method not implemented!")

    def get_main_calculator_file_path(self):
        raise Exception("Abstract method not implemented!")

    def get_input_file_parser(self):
        raise Exception("Abstract method not implemented!")

    def _load_file_content(self):
        file_path = self.get_main_calculator_file_path()
        return InputReader.read_input(file_path)


def _print_separator():
    print("=" * 40)
