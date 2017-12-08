import pytest

from .direction import Direction
from .spiral import Spiral


@pytest.fixture
def spiral():
    return Spiral()


def test_get_last_number_of_empty_spiral(spiral):
    assert 1 == spiral.get_last_number()


def test_get_last_number_after_generating_number(spiral):
    spiral.generate_number()
    assert 2 == spiral.get_last_number()


def test_direction_after_first_number(spiral):
    spiral.generate_number()
    assert Direction.UP == spiral._current_direction


def test_direction_after_two_numbers(spiral):
    spiral.generate_number()
    spiral.generate_number()
    assert Direction.LEFT == spiral._current_direction


def test_direction_after_three_numbers(spiral):
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    assert Direction.LEFT == spiral._current_direction


def test_direction_after_four_numbers(spiral):
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    assert Direction.DOWN == spiral._current_direction


def test_direction_after_eight_numbers(spiral):
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    assert Direction.RIGHT == spiral._current_direction


def test_direction_after_nine_numbers(spiral):
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    assert Direction.UP == spiral._current_direction


def test_get_distance_of_empty_spiral(spiral):
    assert 0 == spiral.get_last_number_distance()


def test_get_distance_of_one_number(spiral):
    spiral.generate_number()
    assert 1 == spiral.get_last_number_distance()


def test_get_distance_of_two_numbers(spiral):
    spiral.generate_number()
    spiral.generate_number()
    assert 2 == spiral.get_last_number_distance()


def test_get_distance_of_three_numbers(spiral):
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    assert 1 == spiral.get_last_number_distance()


# TODO create some way how to dynamically generate numbers
def test_get_distance_of_21_numbers(spiral):
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    spiral.generate_number()
    assert 3 == spiral.get_last_number_distance()
