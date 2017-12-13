import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_1_full_example(solver):
    assert 5 == solver.solve_1([0, 3, 0, 1, -3])


@pytest.mark.skip
def test_2_full_example(solver):
    assert 10 == solver.solve_2([0, 3, 0, 1, -3])
