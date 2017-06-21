import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


# TODO
@pytest.mark.skip
def test_1_full_example(solver):
    assert solver.solve_1("ADVENT") == 6
    assert solver.solve_1("A(1x5)BC") == 7
    assert solver.solve_1("(3x3)XYZ") == 9
    assert solver.solve_1("A(2x2)BCD(2x2)EFG") == 11
    assert solver.solve_1("(6x1)(1x3)A") == 6
    assert solver.solve_1("X(8x2)(3x3)ABCY") == 18


def test_1_1(solver):
    # TODO
    assert solver.solve_1("") == 0


def test_2_1(solver):
    # TODO
    assert solver.solve_2("test test") == 0
