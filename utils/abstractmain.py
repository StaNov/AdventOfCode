from utils import InputReader


class AbstractMain:
    def __init__(self, solver, file):
        self.solver = solver
        self.file = file

    def main_1(self):
        self._load_file_content()
        return self.solver.solve_1()

    def main_2(self):
        self._load_file_content()
        return self.solver.solve_2()

    def _load_file_content(self):
        content = InputReader.read_input(self.file)
        self.solver.input_string = content
