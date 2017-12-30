import pytest

from .solver import Solver

test_input =\
    "7\n"\
    "3\n"\
    "rect 3x2\n"\
    "rotate column x=1 by 1\n"\
    "rotate row y=0 by 4\n"\
    "rotate column x=1 by 1"


@pytest.fixture
def solver():
    return Solver()


def test_1_full_example(solver):
    assert solver.solve_1(test_input) == 6


def test_1_empty_instructions(solver):
    assert solver.solve_1("7\n"
                          "3") == 0


def test_1_single_rect(solver):
    assert solver.solve_1("7\n"
                          "3\n"
                          "rect 3x2") == 6


def test_2_1(solver):
    assert solver.solve_2(test_input) == \
        " X  X X\n"\
        "X X    \n"\
        " X     \n"
