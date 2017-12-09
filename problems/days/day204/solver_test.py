import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_1_full_example(solver):
    assert 2 == solver.solve_1(
        "aa bb cc dd ee\n"
        "aa bb cc dd aa\n"
        "aa bb cc dd aaa")


@pytest.mark.skip
def test_2_full_example(solver):
    assert 3 == solver.solve_2(
        "abcde fghij\n"
        "abcde xyz ecdab\n"
        "a ab abc abd abf abj\n"
        "iiii oiii ooii oooi oooo\n"
        "oiii ioii iioi iiio")
