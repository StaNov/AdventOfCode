import pytest

from .direction import Direction
from .position import Position


@pytest.fixture
def position():
    return Position()


def test_default_position(position):
    assert (0, 0) == position.get_coordinates()


def test_position_if_moved_right(position):
    position.move(Direction.RIGHT)
    assert (1, 0) == position.get_coordinates()


def test_position_if_moved_up(position):
    position.move(Direction.UP)
    assert (0, 1) == position.get_coordinates()


def test_position_if_moved_left(position):
    position.move(Direction.LEFT)
    assert (-1, 0) == position.get_coordinates()


def test_position_if_moved_down(position):
    position.move(Direction.DOWN)
    assert (0, -1) == position.get_coordinates()


def test_get_coordinates_right(position):
    assert (1, 0) == position.get_coordinates_in_direction(Direction.RIGHT)


def test_get_coordinates_up(position):
    assert (0, 1) == position.get_coordinates_in_direction(Direction.UP)


def test_get_coordinates_left(position):
    assert (-1, 0) == position.get_coordinates_in_direction(Direction.LEFT)


def test_get_coordinates_down(position):
    assert (0, -1) == position.get_coordinates_in_direction(Direction.DOWN)
