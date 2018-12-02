import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_1_empty_input_returns_zero(solver):
    assert 0 == solver.solve_1([])


def test_1_positive_number_returns_the_given_number(solver):
    assert 123 == solver.solve_1([123])


def test_1_negative_number_returns_the_given_number(solver):
    assert -456 == solver.solve_1([-456])


def test_1_multiple_numbers_return_their_sum(solver):
    assert 700 == solver.solve_1([1000, -300])


def test_2_zero_is_visited_twice(solver):
    assert 0 == solver.solve_2([1, -1])
