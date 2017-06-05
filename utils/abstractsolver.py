class AbstractSolver:
    def __init__(self, input_string):
        self.solved_was_called = False
        self.input_string = input_string

    def solve_1(self):
        self._check_solved_was_not_called_yet()
        self.solved_was_called = True
        return self.solve_1_internal()

    def solve_2(self):
        self._check_solved_was_not_called_yet()
        self.solved_was_called = True
        return self.solve_2_internal()

    def _check_solved_was_not_called_yet(self):
        if self.solved_was_called:
            raise Exception("Solve call on this object was already called!")
        if self.input_string is None:
            raise Exception("Input string has not been set!")

    def solve_1_internal(self):
        raise Exception("Abstract method not implemented!")

    def solve_2_internal(self):
        raise Exception("Abstract method not implemented!")
