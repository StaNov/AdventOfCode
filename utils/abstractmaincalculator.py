from utils import InputReader


class AbstractMainCalculator:
    def __init__(self):
        self._input_string = self._load_file_content()

    def calculate_both_parts_and_print_results(self):
        result_1 = self.calculate_part_1()
        print("FIRST RESULT IS: " + str(result_1) + " !!!")

        result_2 = self.calculate_part_2()
        print("SECOND RESULT IS: " + str(result_2) + " !!!")

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

    def _load_file_content(self):
        file_path = self.get_main_calculator_file_path()
        return InputReader.read_input(file_path)
