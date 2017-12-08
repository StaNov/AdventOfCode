from .spiralsumming import SpiralSumming


def test_empty_spiral_has_one_as_number():
    assert 1 == SpiralSumming().get_last_number()