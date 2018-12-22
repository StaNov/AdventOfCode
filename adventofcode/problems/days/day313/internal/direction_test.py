from .direction import Direction


def test_apply_direction_down():
    assert Direction.DOWN.apply_on((10, 20)) == (10, 21)
