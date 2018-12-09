import pytest

from .internal import SantaSuitPatch
from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_1_no_patches(solver):
    assert 0 == solver.solve_1([])


def test_1_some_patches(solver):
    assert 2 == solver.solve_1([
        SantaSuitPatch(1, 1, 1, 2, 2),
        SantaSuitPatch(2, 5, 5, 2, 2),
        SantaSuitPatch(3, 2, 2, 2, 2),
        SantaSuitPatch(4, 6, 6, 2, 2),
    ])


def test_2_one_patch(solver):
    assert 1 == solver.solve_2([
        SantaSuitPatch(1, 1, 1, 2, 2),
    ])
