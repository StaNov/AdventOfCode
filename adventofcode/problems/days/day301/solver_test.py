import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_1_empty_input_is_zero_result(solver):
    assert 0 == solver.solve_1([])


def test_1_input_with_one_gives_one_as_result(solver):
    assert 1 == solver.solve_1(["+1"])


def test_1_input_with_two_gives_two_as_result(solver):
    assert 2 == solver.solve_1(["+2"])


def test_1_multiple_digits_input(solver):
    assert 123 == solver.solve_1(["+123"])


def test_1_one_negative_number(solver):
    assert -456 == solver.solve_1(["-456"])


def test_1_two_numbers_sum(solver):
    assert 700 == solver.solve_1(["+1000", "-300"])


def test_2_full_example(solver):
    # TODO
    assert 0 == solver.solve_2("test test")
