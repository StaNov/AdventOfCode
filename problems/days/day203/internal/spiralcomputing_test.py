import pytest

from . import SpiralComputing


def test_spiral_one_has_zero_length():
    assert SpiralComputing(1).distance_from_start() == 0


def test_spiral_two_has_one_length():
    assert SpiralComputing(2).distance_from_start() == 1


def test_spiral_three_has_one_length():
    assert SpiralComputing(3).distance_from_start() == 2


def test_spiral_four_has_one_length():
    assert SpiralComputing(4).distance_from_start() == 1


def test_spiral_five_has_one_length():
    assert SpiralComputing(5).distance_from_start() == 2


def test_spiral_six_has_one_length():
    assert SpiralComputing(6).distance_from_start() == 1


def test_spiral_eleven_has_two_length():
    assert SpiralComputing(11).distance_from_start() == 2


def test_spiral_twelve_has_three_length():
    assert SpiralComputing(12).distance_from_start() == 3


def test_last_number_in_loop_1():
    assert SpiralComputing(1)._last_number_in_loop == 1


def test_last_number_in_loop_2():
    assert SpiralComputing(2)._last_number_in_loop == 9


def test_last_number_in_loop_14():
    assert SpiralComputing(14)._last_number_in_loop == 25


def test_loop_number_1():
    assert SpiralComputing(1)._loop_number == 0


def test_loop_number_5():
    assert SpiralComputing(5)._loop_number == 1


def test_loop_number_22():
    assert SpiralComputing(22)._loop_number == 2


def test_corner_numbers_1():
    assert SpiralComputing(1)._corner_numbers == {1}


def test_corner_numbers_8():
    assert SpiralComputing(8)._corner_numbers == {9, 7, 5, 3}


def test_corner_numbers_16():
    assert SpiralComputing(16)._corner_numbers == {13, 17, 21, 25}


def test_distance_from_corner_1():
    assert SpiralComputing(1)._distance_from_corner == 0


def test_distance_from_corner_6():
    assert SpiralComputing(6)._distance_from_corner == 1


def test_distance_from_corner_19():
    assert SpiralComputing(19)._distance_from_corner == 2


def test_with_exception():
    # TODO
    with pytest.raises(Exception):
        raise Exception("Test exception in test")
