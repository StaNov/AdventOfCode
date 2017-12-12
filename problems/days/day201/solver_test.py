import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_1_full_example_1(solver):
    assert solver.solve_1("1122") == 3


def test_1_full_example_2(solver):
    assert solver.solve_1("1111") == 4


def test_1_full_example_3(solver):
    assert solver.solve_1("1234") == 0


def test_1_full_example_4(solver):
    assert solver.solve_1("91212129") == 9


def test_2_full_example_1(solver):
    assert solver.solve_2("1212") == 6


def test_2_full_example_2(solver):
    assert solver.solve_2("1221") == 0


def test_2_full_example_3(solver):
    assert solver.solve_2("123425") == 4


def test_2_full_example_4(solver):
    assert solver.solve_2("123123") == 12


def test_2_full_example_5(solver):
    assert solver.solve_2("12131415") == 4
