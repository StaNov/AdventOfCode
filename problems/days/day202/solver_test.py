import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_1_1(solver):
    # TODO
    assert solver.solve_1("test test") == 0


@pytest.mark.skip
def test_1_full_example_row_1(solver):
    assert solver.solve_1("5 1 9 5") == 8


@pytest.mark.skip
def test_1_full_example_row_2(solver):
    assert solver.solve_1("7 5 3") == 4


@pytest.mark.skip
def test_1_full_example_row_3(solver):
    assert solver.solve_1("2 4 6 8") == 6


@pytest.mark.skip
def test_1_full_example(solver):
    assert solver.solve_1("5 1 9 5\n7 5 3\n2 4 6 8") == 18


def test_2_1(solver):
    # TODO
    assert solver.solve_2("test test") == 0


def test_2_full_example(solver):
    # TODO
    assert solver.solve_2("test test") == 0
