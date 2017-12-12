import pytest

from .captchacomputerhalfslice import CaptchaComputerHalfSlice


@pytest.fixture
def captcha_computer():
    return CaptchaComputerHalfSlice()


def test_four_same_numbers(captcha_computer):
    assert captcha_computer.compute_captcha("1111") == 4


def test_two_same_numbers_two_different(captcha_computer):
    assert captcha_computer.compute_captcha("1213") == 2


def test_three_pairs(captcha_computer):
    assert captcha_computer.compute_captcha("123123") == 12
