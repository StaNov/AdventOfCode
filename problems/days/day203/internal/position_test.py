from .position import Position


def test_default_position():
    assert (0, 0) == Position().get_coordinates()
