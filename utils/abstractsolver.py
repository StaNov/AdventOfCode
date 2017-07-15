class AbstractSolver:

    def __init__(self):
        self._already_used = False

    # TODO input string into constructor?
    def solve_1(self, input_string):
        self._check_used_and_set_used()
        return self.solve_1_internal(input_string)

    def solve_2(self, input_string):
        self._check_used_and_set_used()
        return self.solve_2_internal(input_string)

    def _check_used_and_set_used(self):
        if self._already_used:
            raise self.SolverAlreadyUsedException("Solver was already used! Create a new one for another usage.")
        self._already_used = True

    # TODO rename to name with underscore in the front?
    def solve_1_internal(self, input_string):
        raise Exception("Abstract method not implemented!")

    def solve_2_internal(self, input_string):
        raise Exception("Abstract method not implemented!")

    class SolverAlreadyUsedException(Exception):
        pass
