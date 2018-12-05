from . import WordsWithoutOneLetterGenerator


def test_empty_string():
    assert set() == WordsWithoutOneLetterGenerator("").generate()


def test_two_letters_word():
    assert {"a", "b"} == WordsWithoutOneLetterGenerator("ab").generate()


def test_three_letters():
    assert {"ab", "ac", "bc"} == WordsWithoutOneLetterGenerator("abc").generate()


def test_double_letters_dont_generate_more_words():
    assert {"bbc", "abc", "abb"} == WordsWithoutOneLetterGenerator("abbc").generate()
