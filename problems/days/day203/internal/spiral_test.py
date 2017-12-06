import pytest

from . import Spiral


def test_spiral_one_has_zero_length():
    assert Spiral(1).distance_from_start() == 0


def test_spiral_two_has_one_length():
    assert Spiral(2).distance_from_start() == 1


def test_spiral_three_has_one_length():
    assert Spiral(3).distance_from_start() == 2


def test_spiral_four_has_one_length():
    assert Spiral(4).distance_from_start() == 1


def test_spiral_five_has_one_length():
    assert Spiral(5).distance_from_start() == 2


def test_spiral_six_has_one_length():
    assert Spiral(6).distance_from_start() == 1


def test_spiral_eleven_has_two_length():
    assert Spiral(11).distance_from_start() == 2


@pytest.mark.skip
def test_spiral_twelve_has_three_length():
    assert Spiral(12).distance_from_start() == 3


def test_last_number_in_loop_1():
    assert Spiral(1).get_last_number_in_loop() == 1


def test_last_number_in_loop_2():
    assert Spiral(2).get_last_number_in_loop() == 9


def test_last_number_in_loop_14():
    assert Spiral(14).get_last_number_in_loop() == 25


def test_loop_number_1():
    assert Spiral(1).get_loop_number() == 0


def test_with_exception():
    # TODO
    with pytest.raises(Exception):
        raise Exception("Test exception in test")
