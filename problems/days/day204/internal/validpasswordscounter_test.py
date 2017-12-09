import pytest

from . import ValidPasswordsCounter


class TestChecker:
    VALID_LINE = "abc"

    def check(self, password):
        return password == self.VALID_LINE


def test_zero_valid_passwords_in_empty_string():
    assert 0 == ValidPasswordsCounter().count("", TestChecker())


@pytest.mark.skip
def test_one_valid_password():
    assert 1 == ValidPasswordsCounter().count("abc", TestChecker())
