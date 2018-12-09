import pytest

from .internal import SantaSuitPiece
from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_1_no_patches(solver):
    assert 0 == solver.solve_1([])


def test_1_different_position_some_overlap(solver):
    assert 1 == solver.solve_1([
        SantaSuitPiece(1, 1, 1, 2, 2),
        SantaSuitPiece(2, 2, 2, 2, 2),
    ])


# TODO
@pytest.mark.skip
def test_2_something(solver):
    # TODO
    assert 0 == solver.solve_2("test test")
