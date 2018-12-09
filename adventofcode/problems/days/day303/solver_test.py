import pytest

from .internal import SantaSuitPiece
from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_1_no_patches(solver):
    assert 0 == solver.solve_1([])


def test_1_some_patches(solver):
    assert 2 == solver.solve_1([
        SantaSuitPiece(1, 1, 1, 2, 2),
        SantaSuitPiece(2, 5, 5, 2, 2),
        SantaSuitPiece(3, 2, 2, 2, 2),
        SantaSuitPiece(4, 6, 6, 2, 2),
    ])


def test_2_one_patch(solver):
    assert 1 == solver.solve_2([
        SantaSuitPiece(1, 1, 1, 2, 2),
    ])
