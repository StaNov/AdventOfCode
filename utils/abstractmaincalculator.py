from utils import InputReader


class AbstractMainCalculator:
    def __init__(self, solver, file):
        self._solver = solver
        self._file = file
        self._input_string = self._load_file_content()

    def calculate_both_parts_and_print_results(self):
        result_1 = self.calculate_part_1()
        print("FIRST RESULT IS: " + str(result_1) + " !!!")

        result_2 = self.calculate_part_2()
        print("SECOND RESULT IS: " + str(result_2) + " !!!")

    def calculate_part_1(self):
        return self._solver.solve_1(self._input_string)

    def calculate_part_2(self):
        return self._solver.solve_2(self._input_string)

    def _load_file_content(self):
        return InputReader.read_input(self._file)
