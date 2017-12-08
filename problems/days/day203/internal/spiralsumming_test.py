import pytest

from .spiralsumming import SpiralSumming


@pytest.fixture
def spiral():
    return SpiralSumming()


def test_empty_spiral_has_one_as_number(spiral):
    assert 1 == spiral.get_last_number()


def test_empty_spiral_has_one_as_second_number(spiral):
    spiral.generate_number()
    assert 1 == spiral.get_last_number()
