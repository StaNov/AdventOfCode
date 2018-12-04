from . import SameLettersCounter


def test_empty_string_has_no_doubles():
    assert not SameLettersCounter("").has_n_same_letters(2)


def test_two_same_letters():
    assert SameLettersCounter("aa").has_n_same_letters(2)


def test_two_different_letters():
    assert not SameLettersCounter("ab").has_n_same_letters(2)


def test_two_same_letters_far_from_each_other():
    assert SameLettersCounter("aba").has_n_same_letters(2)


def test_three_same_letters_are_not_exactly_two():
    assert not SameLettersCounter("aaa").has_n_same_letters(2)


def test_two_letters_not_first_one():
    assert SameLettersCounter("baa").has_n_same_letters(2)


def test_three_same_letters():
    assert SameLettersCounter("abbba").has_n_same_letters(3)
