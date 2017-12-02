import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


@pytest.mark.skip
def test_1_full_example_1(solver):
    assert solver.solve_1("1122") == 3


@pytest.mark.skip
def test_1_full_example_2(solver):
    assert solver.solve_1("1111") == 4


@pytest.mark.skip
def test_1_full_example_3(solver):
    assert solver.solve_1("1234") == 0


@pytest.mark.skip
def test_1_full_example_4(solver):
    assert solver.solve_1("91212129") == 9


def test_1_zero_sum_when_empty_input(solver):
    assert solver.solve_1("") == 0


def test_1_zero_sum_when_one_character_long_input(solver):
    assert solver.solve_1("2") == 0


def test_1_non_zero_sum_when_two_identical_digits(solver):
    assert solver.solve_1("22") == 2


def test_1_zero_sum_when_two_different_digits(solver):
    assert solver.solve_1("21") == 0


def test_1_non_zero_sum_when_two_same_digits_2(solver):
    assert solver.solve_1("33") == 3


def test_1_non_zero_sum_when_two_same_digits_and_one_different(solver):
    assert solver.solve_1("331") == 3


def test_1_non_zero_sum_when_one_different_digit_and_two_same_ones(solver):
    assert solver.solve_1("133") == 3


def test_1_two_pairs_return_their_sum(solver):
    assert solver.solve_1("12334567789") == 10


def test_2_1(solver):
    # TODO
    assert solver.solve_2("test test") == 0


def test_2_full_example(solver):
    # TODO
    assert solver.solve_2("test test") == 0
