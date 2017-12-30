from . import PasswordCheckerAnagramic, passwordcheckeranagramic as checker


def test_two_anagramic_words_invalid():
    assert not PasswordCheckerAnagramic().check("abcd dcba")


def test_sort_letters_empty_string():
    assert "" == checker._sort_letters_in_word("")


def test_sort_letters_already_sorted():
    assert "abcd" == checker._sort_letters_in_word("abcd")


def test_sort_letters_not_sorted():
    assert "abcd" == checker._sort_letters_in_word("bdca")
