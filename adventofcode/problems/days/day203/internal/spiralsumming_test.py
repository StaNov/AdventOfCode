import pytest

from .spiralsumming import SpiralSumming


@pytest.fixture
def spiral():
    return SpiralSumming()


def test_empty_spiral_has_one_as_number(spiral):
    assert 1 == spiral.get_last_number()


def test_one_as_second_number(spiral):
    spiral.generate_number()
    assert 1 == spiral.get_last_number()


def test_third_number(spiral):
    spiral.generate_numbers(2)
    assert 2 == spiral.get_last_number()


def test_tenth_number(spiral):
    spiral.generate_numbers(10)
    assert 54 == spiral.get_last_number()
