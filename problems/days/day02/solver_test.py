import pytest

from .solver import Solver

@pytest.fixture
def solver():
    return Solver()


def test_1_1(solver):
    assert solver.solve_1("ULL\nRRDDD\nLURDL\nUUUUD") == "1985"


def test_2_1(solver):
    assert solver.solve_2("ULL\nRRDDD\nLURDL\nUUUUD") == "5DB3"
