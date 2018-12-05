import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_2_two_letters(solver):
    assert "a" == solver.solve_2(["ab", "ac"])


def test_2_three_letters(solver):
    assert "ab" == solver.solve_2(["abc", "abd"])


def test_2_three_letters_another_order(solver):
    assert "ac" == solver.solve_2(["axc", "ayc"])
