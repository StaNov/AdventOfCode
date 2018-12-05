import pytest

from . import WordsWithoutOneLetterGenerator


@pytest.fixture
def generator():
    return WordsWithoutOneLetterGenerator()


def test_empty_string(generator):
    assert set() == generator.generate("")


def test_two_letters_word(generator):
    assert {"a", "b"} == generator.generate("ab")


def test_three_letters(generator):
    assert {"ab", "ac", "bc"} == generator.generate("abc")


def test_double_letters_dont_generate_more_words(generator):
    assert {"bbc", "abc", "abb"} == generator.generate("abbc")
