import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_1_full_example_1(solver):
    assert 0 == solver.solve_1("1")


def test_1_full_example_2(solver):
    assert 3 == solver.solve_1("12")


def test_1_full_example_3(solver):
    assert 2 == solver.solve_1("23")


def test_1_full_example_4(solver):
    assert 31 == solver.solve_1("1024")


def test_2_full_example_1(solver):
    assert 1 == solver.solve_2("0")


def test_2_full_example_2(solver):
    assert 2 == solver.solve_2("1")


def test_2_full_example_3(solver):
    assert 4 == solver.solve_2("2")


def test_2_full_example_4(solver):
    assert 5 == solver.solve_2("4")
