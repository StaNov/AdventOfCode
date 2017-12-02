import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


@pytest.mark.skip
def test_1_full_example_1(solver):
    assert solver.solve_1("1122") == 3


@pytest.mark.skip
def test_1_full_example_2(solver):
    assert solver.solve_1("1111") == 4


@pytest.mark.skip
def test_1_full_example_3(solver):
    assert solver.solve_1("1234") == 0


@pytest.mark.skip
def test_1_full_example_4(solver):
    assert solver.solve_1("91212129") == 9


def test_2_1(solver):
    # TODO
    assert solver.solve_2("test test") == 0


def test_2_full_example(solver):
    # TODO
    assert solver.solve_2("test test") == 0
