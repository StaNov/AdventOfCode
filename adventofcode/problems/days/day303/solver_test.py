import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_1_no_patches(solver):
    assert 0 == solver.solve_1([])


def test_2_something(solver):
    # TODO
    assert 0 == solver.solve_2("test test")
