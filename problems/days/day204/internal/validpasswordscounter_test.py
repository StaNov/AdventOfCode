import pytest

from . import ValidPasswordsCounter


class TestChecker:
    VALID_LINE = "validPassword"

    def check(self, password):
        return password == self.VALID_LINE


@pytest.fixture
def checker():
    return TestChecker()


@pytest.fixture
def counter(checker):
    return ValidPasswordsCounter(checker)


def test_zero_valid_passwords_in_empty_string(counter):
    assert 0 == counter.count("")


def test_one_valid_password(counter):
    assert 1 == counter.count("validPassword")


def test_one_invalid_password(counter):
    assert 0 == counter.count("invalid")


def test_two_valid_passwords(counter):
    assert 2 == counter.count("validPassword\nvalidPassword")


def test_valid_and_invalid_passwords(counter):
    assert 1 == counter.count("validPassword\ninvalid")
