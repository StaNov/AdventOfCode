class AbstractSolver:
    def solve_1(self, input_string):
        self._initialize()
        return self.solve_1_internal(input_string)

    def solve_2(self, input_string):
        self._initialize()
        return self.solve_2_internal(input_string)

    def _initialize(self):
        self.initialize_internal()

    # TODO rename to name with underscore in the front?
    def solve_1_internal(self, input_string):
        raise Exception("Abstract method not implemented!")

    def solve_2_internal(self, input_string):
        raise Exception("Abstract method not implemented!")

    def initialize_internal(self):
        raise Exception("Abstract method not implemented!")
