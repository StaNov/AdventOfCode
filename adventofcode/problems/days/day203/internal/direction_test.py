from .direction import Direction


def test_rotate_just_like_that():
    assert Direction.UP == Direction.RIGHT.rotate_left()


def test_rotate_last_to_first():
    assert Direction.DOWN == Direction.LEFT.rotate_left()
