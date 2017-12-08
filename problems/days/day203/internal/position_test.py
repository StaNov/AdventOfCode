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
