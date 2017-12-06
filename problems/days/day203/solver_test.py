import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_1_full_example_1(solver):
    assert solver.solve_1("1") == 0


def test_1_full_example_2(solver):
    assert solver.solve_1("12") == 3


def test_1_full_example_3(solver):
    assert solver.solve_1("23") == 2


def test_1_full_example_4(solver):
    assert solver.solve_1("1024") == 31


def test_2_1(solver):
    # TODO
    assert solver.solve_2("test test") == 0


def test_2_full_example(solver):
    # TODO
    assert solver.solve_2("test test") == 0
