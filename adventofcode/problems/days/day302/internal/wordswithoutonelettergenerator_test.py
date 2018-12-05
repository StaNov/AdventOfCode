import pytest

from . import WordsWithoutOneLetterGenerator


@pytest.fixture
def generator():
    return WordsWithoutOneLetterGenerator()


def test_empty_string(generator):
    assert [] == generator.generate("")


def test_two_letters_word(generator):
    assert ["a", "b"] == generator.generate("ab")
