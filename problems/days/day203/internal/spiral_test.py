import pytest

from . import Spiral


def test_spiral_one_has_zero_length():
    assert Spiral(1).distance_from_start() == 0


def test_spiral_two_has_one_length():
    assert Spiral(2).distance_from_start() == 1


def test_with_exception():
    # TODO
    with pytest.raises(Exception):
        raise Exception("Test exception in test")
