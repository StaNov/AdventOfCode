from .direction import Direction


def test_apply_direction_down():
    assert Direction.DOWN.apply_on((10, 20)) == (10, 21)


def test_apply_direction_up():
    assert Direction.UP.apply_on((10, 20)) == (10, 19)


def test_apply_direction_right():
    assert Direction.RIGHT.apply_on((10, 20)) == (11, 20)
