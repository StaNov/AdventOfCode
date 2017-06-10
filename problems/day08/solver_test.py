import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


@pytest.mark.skip
def test_1_full_example(solver):
    assert solver.solve_1("7\n"
                          "3\n"
                          "rect 3x2\n"
                          "rotate column x=1 by 1\n"
                          "rotate row y=0 by 4\n"
                          "rotate column x=1 by 1\n") == 6


def test_1_empty_instructions(solver):
    assert solver.solve_1("7\n"
                          "3") == 0


def test_1_single_rect(solver):
    assert solver.solve_1("7\n"
                          "3\n"
                          "rect 3x2") == 6


@pytest.mark.skip
def test_2_1(solver):
    # TODO
    assert solver.solve_2("test test") == 0
