import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_1_full_example_row_1(solver):
    assert solver.solve_1("5 1 9 5") == 8


def test_1_full_example_row_2(solver):
    assert solver.solve_1("7 5 3") == 4


def test_1_full_example_row_3(solver):
    assert solver.solve_1("2 4 6 8") == 6


def test_1_full_example(solver):
    assert solver.solve_1("5 1 9 5\n7 5 3\n2 4 6 8") == 18


def test_2_full_example_1(solver):
    assert solver.solve_2("5 9 2 8") == 4


def test_2_full_example_2(solver):
    assert solver.solve_2("9 4 7 3") == 3


def test_2_full_example_3(solver):
    assert solver.solve_2("3 8 6 5") == 2


def test_2_full_example_4(solver):
    assert solver.solve_2("5 9 2 8\n9 4 7 3\n3 8 6 5") == 9
