import time

import pytest

from adventofcode.problems.framework import testsuite
from . import OreMine


def test_create_empty_ore_mine():
    cars = OreMine([]).cars
    assert 0 == len(cars)


def test_with_exception():
    # TODO
    with pytest.raises(Exception):
        raise Exception("Test exception in test")


@testsuite.time_expensive
def test_time_expensive_test():
    time.sleep(1)
