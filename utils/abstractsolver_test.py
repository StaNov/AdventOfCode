import pytest

from . import *


@pytest.fixture
def solver():
    class DummySolver(AbstractSolver):
        def solve_2_internal(self, input_string):
            return 0

        def solve_1_internal(self, input_string):
            return 0

    return DummySolver()


def test_multiple_solving_by_one_solver_raises_exception(solver):
    solver.solve_1("test")
    with pytest.raises(AbstractSolver.SolverAlreadyUsedException):
        solver.solve_2("test")
