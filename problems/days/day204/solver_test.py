import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


@pytest.mark.skip
def test_1_full_example_1(solver):
    assert solver.solve_1("aa bb cc dd ee") == 1


@pytest.mark.skip
def test_1_full_example_2(solver):
    assert solver.solve_1("aa bb cc dd aa") == 0


@pytest.mark.skip
def test_1_full_example_3(solver):
    assert solver.solve_1("aa bb cc dd aaa") == 1


@pytest.mark.skip
def test_1_full_example_4(solver):
    assert solver.solve_1("aa bb cc dd ee\naa bb cc dd aa\naa bb cc dd aaa") == 2


def test_2_1(solver):
    # TODO
    assert solver.solve_2("test test") == 0


def test_2_full_example(solver):
    # TODO
    assert solver.solve_2("test test") == 0
