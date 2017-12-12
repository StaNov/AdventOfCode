import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


# TODO
@pytest.mark.skip
def test_1_full_example(solver):
    assert 5 == solver.solve_1([0, 3, 0, 1, -3])


def test_2_full_example(solver):
    # TODO
    assert solver.solve_2("test test") == 0
