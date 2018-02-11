class AbstractSolver:

    def __init__(self):
        self._already_used = False

    # TODO input string into constructor?
    def solve_1(self, input_):
        self._check_used_and_set_used()
        return self._solve_1_internal(input_)

    def solve_2(self, input_):
        self._check_used_and_set_used()
        return self._solve_2_internal(input_)

    def _check_used_and_set_used(self):
        if self._already_used:
            raise self.SolverAlreadyUsedException("Solver was already used! Create a new one for another usage.")
        self._already_used = True

    def _solve_1_internal(self, input_):
        raise NotImplementedError("Abstract method not implemented!")

    def _solve_2_internal(self, input_):
        raise NotImplementedError("Abstract method not implemented!")

    class SolverAlreadyUsedException(Exception):
        pass
