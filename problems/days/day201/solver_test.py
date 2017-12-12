import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_1_exception_when_empty_input(solver):
    with pytest.raises(Exception):
        solver.solve_1("")


def test_1_exception_when_one_char(solver):
    with pytest.raises(Exception):
        solver.solve_1("1")


def test_1_exception_when_two_chars(solver):
    with pytest.raises(Exception):
        solver.solve_1("1")


def test_1_non_zero_sum_when_two_same_digits_and_one_different(solver):
    assert solver.solve_1("331") == 3


def test_1_non_zero_sum_when_one_different_digit_and_two_same_ones(solver):
    assert solver.solve_1("133") == 3


def test_1_two_pairs_return_their_sum(solver):
    assert solver.solve_1("12334567789") == 10


def test_1_two_pairs_return_their_sum_circular(solver):
    assert solver.solve_1("1233451") == 4


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
