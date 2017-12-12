import pytest

from . import CaptchaComputer


@pytest.fixture
def captcha_computer():
    return CaptchaComputer()


def test_exception_when_empty_input(captcha_computer):
    with pytest.raises(Exception):
        captcha_computer.compute_captcha("")


def test_exception_when_one_char(captcha_computer):
    with pytest.raises(Exception):
        captcha_computer.compute_captcha("1")


def test_exception_when_two_chars(captcha_computer):
    with pytest.raises(Exception):
        captcha_computer.compute_captcha("12")


def test_non_zero_sum_when_two_same_digits_and_one_different(captcha_computer):
    assert captcha_computer.compute_captcha("331") == 3


def test_non_zero_sum_when_one_different_digit_and_two_same_ones(captcha_computer):
    assert captcha_computer.compute_captcha("133") == 3


def test_two_pairs_return_their_sum(captcha_computer):
    assert captcha_computer.compute_captcha("12334567789") == 10


def test_two_pairs_return_their_sum_circular(captcha_computer):
    assert captcha_computer.compute_captcha("1233451") == 4
