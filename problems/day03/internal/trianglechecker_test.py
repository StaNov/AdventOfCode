from . import TriangleChecker


def test_check_true():
    assert TriangleChecker.check(4, 5, 6)


def test_check_false():
    assert not TriangleChecker.check(1, 50, 60)
