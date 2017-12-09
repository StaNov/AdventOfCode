import pytest

from . import PasswordChecker


@pytest.fixture
def checker():
    return PasswordChecker()


def test_empty_password_is_valid(checker):
    assert checker.check("")


def test_with_exception():
    # TODO
    with pytest.raises(Exception):
        raise Exception("Test exception in test")
