import pytest

from . import PasswordChecker


@pytest.fixture
def checker():
    return PasswordChecker()


def test_empty_password_is_valid(checker):
    assert checker.check("")


def test_two_same_words_are_invalid(checker):
    assert not checker.check("abc abc")


def test_one_word_is_valid(checker):
    assert checker.check("abc")


def test_two_different_words_are_valid(checker):
    assert checker.check("abc def")
