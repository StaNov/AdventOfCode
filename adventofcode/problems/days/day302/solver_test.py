import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


# TODO
@pytest.mark.skip
def test_1_full_example(solver):
    # TODO
    assert 0 == solver.solve_1("test test")


# TODO
@pytest.mark.skip
def test_2_full_example(solver):
    # TODO
    assert 0 == solver.solve_2("test test")
