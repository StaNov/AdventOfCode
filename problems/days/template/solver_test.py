import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_1_full_example(solver):
    # TODO
    assert solver.solve_1("test test") == 0


def test_2_full_example(solver):
    # TODO
    assert solver.solve_2("test test") == 0
