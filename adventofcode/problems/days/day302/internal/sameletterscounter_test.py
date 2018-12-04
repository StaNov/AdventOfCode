import time

import pytest

from adventofcode.problems.framework import testsuite
from . import SameLettersCounter


def test_empty_string_has_no_doubles():
    assert not SameLettersCounter("").has_two_same_letters()


def test_two_same_letters():
    assert SameLettersCounter("aa").has_two_same_letters()


def test_two_different_letters():
    assert not SameLettersCounter("ab").has_two_same_letters()


def test_two_same_letters_far_from_each_other():
    assert SameLettersCounter("aba").has_two_same_letters()


def test_three_same_letters_are_not_exactly_two():
    assert not SameLettersCounter("aaa").has_two_same_letters()


def test_two_letters_not_first_one():
    assert SameLettersCounter("baa").has_two_same_letters()


def test_with_exception():
    # TODO
    with pytest.raises(Exception):
        raise Exception("Test exception in test")


@testsuite.time_expensive
@pytest.mark.skip
def test_time_expensive_test():
    time.sleep(1)
