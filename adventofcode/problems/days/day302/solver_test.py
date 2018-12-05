import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_2_two_words(solver):
    # TODO
    assert "a" == solver.solve_2(["ab", "ac"])
