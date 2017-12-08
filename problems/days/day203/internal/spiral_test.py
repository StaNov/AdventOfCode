import pytest

from .spiral import Spiral


@pytest.fixture
def spiral():
    return Spiral()


def test_get_last_number_of_empty_spiral(spiral):
    assert 1 == spiral.get_last_number()


def test_get_last_number_after_generating_number(spiral):
    spiral.generate_number()
    assert 2 == spiral.get_last_number()


def test_get_distance_of_empty_spiral(spiral):
    assert 0 == spiral.get_last_number_distance()


def test_get_distance_of_one_number(spiral):
    spiral.generate_number()
    assert 1 == spiral.get_last_number_distance()


def test_get_distance_of_two_numbers(spiral):
    spiral.generate_number()
    spiral.generate_number()
    assert 2 == spiral.get_last_number_distance()


@pytest.mark.skip
def test_get_distance_of_three_numbers(spiral):
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    assert 1 == spiral.get_last_number_distance()
