from . import WordsWithoutOneLetterGenerator


def test_empty_string():
    assert [] == WordsWithoutOneLetterGenerator().generate("")
