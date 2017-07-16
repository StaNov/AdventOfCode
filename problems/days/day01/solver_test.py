import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_1_1(solver):
    assert solver.solve_1("R2, L3") == 5


def test_1_2(solver):
    assert solver.solve_1("R2, R2, R2") == 2


def test_1_3(solver):
    assert solver.solve_1("R5, L5, R5, R3") == 12


def test_2_1(solver):
    assert solver.solve_2("R8, R4, R4, R8") == 4
