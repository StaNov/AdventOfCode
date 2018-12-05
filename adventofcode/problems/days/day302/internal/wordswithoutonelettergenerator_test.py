import pytest

from . import WordsWithoutOneLetterGenerator


@pytest.fixture
def generator():
    return WordsWithoutOneLetterGenerator()


def test_empty_string(generator):
    assert [] == generator.generate("")
